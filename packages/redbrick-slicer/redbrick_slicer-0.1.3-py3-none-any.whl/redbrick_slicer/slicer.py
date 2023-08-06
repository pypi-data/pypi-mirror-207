"""Main object for RedBrick SDK."""
import math
import os
import json
import re
import gzip
import random
from typing import Dict, List, no_type_check
from uuid import uuid4
import asyncio

import qt  # type: ignore
import slicer  # type: ignore
from DICOMLib import DICOMUtils  # type: ignore

from redbrick_slicer.common.context import RBContext
from redbrick_slicer.project import RBProject
from redbrick_slicer.utils.files import download_files
from redbrick_slicer.utils.url import generate_task_url, tool_url_parse


# pylint: skip-file


class RBSlicer:
    """Interact with a RedBrick task in 3D Slicer application."""

    def __init__(self, context: RBContext, url: str) -> None:
        """Construct RBProject."""
        self.context = context
        self.url = url

        self.org_id, self.project_id, self.task_id, self.stage_name = tool_url_parse(
            self.url
        )
        self.project = RBProject(self.context, self.org_id, self.project_id)

        self.segments: List[str] = []
        self.segment_color_map: Dict[str, List[int]] = {}

        self.root = os.path.join(os.path.expanduser("~"), ".redbrick-slicer")
        self.org_dir = os.path.join(self.root, str(self.org_id))
        self.project_dir = os.path.join(self.org_dir, str(self.project_id))
        self.task_dir = os.path.join(self.project_dir, str(self.task_id))

        self.data_dir = os.path.join(self.task_dir, "data")
        os.makedirs(self.data_dir, exist_ok=True)

        self.other_labels: List[Dict] = []

    @staticmethod
    def _get_categories(category: Dict) -> List[str]:
        category_names = [category["name"]]
        for child in category.get("children", []):
            category_names += [
                category_names[0] + "::" + name
                for name in RBSlicer._get_categories(child)
            ]
        return category_names

    def _cat2cat(self, cat_name: str, cat_id: int, colormap: List[Dict]) -> Dict:
        for val in colormap:
            if val["trail"] and "::".join(val["trail"][1:]) == cat_name:
                self.segment_color_map[cat_name] = [
                    int(val["color"][i : i + 2], 16) for i in (1, 3, 5)
                ]
                break
        else:
            self.segment_color_map[cat_name] = [
                random.randint(0, 255) for _ in range(3)
            ]

        return {
            "recommendedDisplayRGBValue": self.segment_color_map[cat_name],
            "CodeMeaning": cat_name,
            "CodingSchemeDesignator": "SCT",
            "3dSlicerLabel": cat_name,
            "3dSlicerIntegerLabel": cat_id,
            "cid": str(cat_id),
            "UMLSConceptUID": "C0344335",
            "CodeValue": str(cat_id),
            "contextGroupName": "CommonTissueSegmentationTypes",
            "SNOMEDCTConceptID": str(cat_id),
        }

    def _cat2catNew(self, category: Dict, cat_id: int) -> Dict:
        self.segment_color_map[category["category"]] = [
            int(category["color"][i : i + 2], 16) for i in (1, 3, 5)
        ]
        return {
            "recommendedDisplayRGBValue": self.segment_color_map[category["category"]],
            "CodeMeaning": category["category"],
            "CodingSchemeDesignator": "SCT",
            "3dSlicerLabel": category["category"],
            "3dSlicerIntegerLabel": cat_id,
            "cid": str(cat_id),
            "UMLSConceptUID": "C0344335",
            "CodeValue": str(cat_id),
            "contextGroupName": "CommonTissueSegmentationTypes",
            "SNOMEDCTConceptID": str(cat_id),
        }

    @no_type_check
    def get_task(self) -> None:
        """Get task for labeling."""
        task, taxonomy = self.project.export.get_raw_data_single(self.task_id)

        if taxonomy.get("isNew"):
            self.segments = [
                cat["category"]
                for cat in taxonomy["objectTypes"]
                if cat["labelType"] == "SEGMENTATION" and not cat.get("archived")
            ]
        else:
            parent_cat = taxonomy.get("categories", [])
            if len(parent_cat) == 1 and parent_cat[0]["name"] == "object":
                for child in parent_cat[0]["children"]:
                    self.segments += RBSlicer._get_categories(child)

        if not self.segments:
            print("Unsupported taxonomy")
            return

        taxName = re.sub(r"[^a-zA-Z]", "", taxonomy["name"])
        is_tax_v2 = bool(taxonomy.get("isNew"))

        print("Taxonomy:", taxName)
        print("Available categories:", self.segments)
        print("Task ID:", self.task_id)
        print("Please use corresponding segmentation and source volumes")

        slicer.mrmlScene.Clear(0)

        term_json_file = os.path.join(self.project_dir, "terminologies.json")
        term_json = {
            "SegmentationCategoryTypeContextName": taxName,
            "@schema": "https://raw.githubusercontent.com/qiicr/dcmqi/master/doc/segment-context-schema.json#",
            "SegmentationCodes": {
                "Category": [
                    {
                        "CodeMeaning": "Categories",
                        "CodingSchemeDesignator": "SCT",
                        "showAnatomy": True,
                        "cid": "7150",
                        "CodeValue": "85756007",
                        "contextGroupName": "SegmentationPropertyCategories",
                        "Type": [
                            self._cat2catNew(
                                [
                                    obj_type
                                    for obj_type in taxonomy["objectTypes"]
                                    if obj_type["labelType"] == "SEGMENTATION"
                                    and not obj_type.get("archived")
                                    and obj_type["category"] == cat
                                ][0],
                                idx + 1,
                            )
                            if is_tax_v2
                            else self._cat2cat(cat, idx + 1, taxonomy["colorMap"])
                            for idx, cat in enumerate(self.segments)
                        ],
                    }
                ],
            },
        }

        with open(term_json_file, "w", encoding="utf-8") as file_:
            json.dump(term_json, file_, indent=2)

        termLogic = slicer.util.getModuleLogic("Terminologies")
        termLogic.LoadTerminologyFromFile(term_json_file)

        slicer.app.settings().setValue("Terminology/LastTerminologyContext", taxName)
        defaultCat = f"{taxName}~SCT^85756007^Categories~^^~^^~Anatomic codes - DICOM master list~^^~^^"
        slicer.app.settings().setValue(
            "Segmentations/DefaultTerminologyEntry", defaultCat
        )

        loop = asyncio.get_event_loop()
        if len(task["items"]) == 1 and ".nii" in task["items"][0]:
            path = os.path.join(
                self.data_dir,
                "vol_"
                + str(self.task_id)
                + ".nii"
                + (".gz" if ".nii.gz" in task["items"][0] else ""),
            )
            if not os.path.isfile(path):
                loop.run_until_complete(
                    download_files([(task["itemsPresigned"][0], path)])
                )
            slicer.util.loadVolume(path)
        else:
            files = []
            for idx, item in enumerate(task["itemsPresigned"]):
                path = os.path.join(self.data_dir, f"{idx}.dcm")
                if not os.path.isfile(path):
                    files.append((item, path))

            loop.run_until_complete(download_files(files))

            with DICOMUtils.TemporaryDICOMDatabase() as db:
                DICOMUtils.importDicom(self.data_dir, db)
                patientUIDs = db.patients()
                assert len(patientUIDs) == 1, "Failed to load data"
                DICOMUtils.loadPatientByUID(patientUIDs[0])

        if task["labelsPath"]:
            labels_path = os.path.join(
                self.task_dir, "seg_" + str(self.task_id) + ".nii"
            )
            if os.path.isfile(labels_path):
                os.remove(labels_path)
            loop.run_until_complete(download_files([(task["labelsPath"], labels_path)]))

            slicer.util.loadSegmentation(labels_path)
            segmentationNode = slicer.mrmlScene.GetFirstNodeByClass(
                "vtkMRMLSegmentationNode"
            )

        else:
            segmentationNode = slicer.vtkMRMLSegmentationNode()
            slicer.mrmlScene.AddNode(segmentationNode)

        slicer.util.selectModule("SegmentEditor")
        segmentationNode = slicer.mrmlScene.GetFirstNodeByClass(
            "vtkMRMLSegmentationNode"
        )

        rb_segmentation = segmentationNode.GetSegmentation()
        labels = sorted(
            (label for label in task["labels"] if label.get("dicom")),
            key=lambda label: label["dicom"]["instanceid"],
        )
        self.other_labels = [
            label for label in task["labels"] if not label.get("dicom")
        ]

        all_segments = set()
        for label in labels:
            all_segments.add(label["dicom"]["instanceid"])
            if label["dicom"].get("groupids"):
                all_segments |= set(label["dicom"]["groupids"])
        all_segments_map = {
            segment: idx + 1 for idx, segment in enumerate(sorted(all_segments))
        }

        label_rb_map = {}
        for label in labels:
            label["dicom"]["slicer:segmentid"] = all_segments_map[
                label["dicom"]["instanceid"]
            ]
            label_rb_map[label["dicom"]["instanceid"]] = (
                label["category"] if is_tax_v2 else "::".join(label["category"][0][1:])
            )
        for label in labels:
            if label["dicom"].get("groupids"):
                for groupid in label["dicom"]["groupids"]:
                    label_rb_map[groupid] = label_rb_map.get(groupid, "")
                    label_rb_map[groupid] += (
                        ("+" if label_rb_map[groupid] else "")
                        + label_rb_map[label["dicom"]["instanceid"]]
                        + "#"
                        + str(label["dicom"]["slicer:segmentid"])
                    )

        display = segmentationNode.GetDisplayNode()
        for num in range(rb_segmentation.GetNumberOfSegments()):
            seg = rb_segmentation.GetNthSegment(num)
            display.SetSegmentVisibility(rb_segmentation.GetNthSegmentID(num), True)
            val = seg.GetLabelValue()
            if val in label_rb_map:
                seg.SetName(label_rb_map[val])
                if label_rb_map[val] in self.segment_color_map:
                    seg.SetColor(
                        tuple(
                            map(
                                lambda color: color / 255,
                                self.segment_color_map[label_rb_map[val]],
                            )
                        )
                    )
                elif "+" in label_rb_map[val]:
                    sub_instances_names = [
                        sub_instance_name.split("#")[0]
                        for sub_instance_name in label_rb_map[val].split("+")
                    ]
                    if all(
                        sub_instance_name in self.segment_color_map
                        for sub_instance_name in sub_instances_names
                    ):
                        red, green, blue = 0, 0, 0
                        for sub_instance_name in sub_instances_names:
                            red += self.segment_color_map[sub_instance_name][0] ** 2
                            green += self.segment_color_map[sub_instance_name][1] ** 2
                            blue += self.segment_color_map[sub_instance_name][2] ** 2
                        red = math.floor(math.sqrt(red / len(sub_instances_names)))
                        green = math.floor(math.sqrt(green / len(sub_instances_names)))
                        blue = math.floor(math.sqrt(blue / len(sub_instances_names)))
                        seg.SetColor((red / 255, green / 255, blue / 255))

        sliceController = (
            slicer.app.layoutManager().sliceWidget("Red").sliceController()
        )
        save_btn = qt.QPushButton("Save")
        submit_btn = qt.QPushButton("Submit")
        exit_btn = qt.QPushButton("Exit")

        save_btn.clicked.connect(self.handle_save)
        submit_btn.clicked.connect(self.handle_submit)
        exit_btn.clicked.connect(self.handle_exit)

        barLayout = sliceController.barLayout()
        child = 0
        while True:
            if barLayout.itemAt(child) is None:
                break
            widget = barLayout.itemAt(child).widget()
            if isinstance(widget, qt.QPushButton) and widget.text in (
                "Save",
                "Submit",
                "Exit",
            ):
                barLayout.removeWidget(widget)
            else:
                child += 1

        barLayout.addWidget(save_btn)
        barLayout.addWidget(submit_btn)
        barLayout.addWidget(exit_btn)

    def handle_save(self) -> None:
        """Save button handler."""
        print("Saving...")
        self.save_data(False)
        print("Saved")

    def handle_submit(self) -> None:
        """Submit button handler."""
        print("Submitting...")
        self.save_data(True)
        print(generate_task_url(self.url))

    def handle_exit(self) -> None:
        """Reset button handler."""
        print("Exiting...")
        slicer.mrmlScene.Clear(0)

    @no_type_check
    def save_data(self, finished: bool) -> None:
        """Save data for task."""
        import numpy as np
        import nibabel as nb  # type: ignore

        scene = slicer.mrmlScene

        segmentationNode = scene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
        rb_segmentation = segmentationNode.GetSegmentation()
        labels = {}
        for num in range(rb_segmentation.GetNumberOfSegments()):
            seg = rb_segmentation.GetNthSegment(num)
            name = seg.GetName()
            if name not in self.segments and "+" not in name:
                print(f"Category: `{name}` not found. Skipping")
                continue
            val = num + 1  # seg.GetLabelValue()
            labels[name + "#" + str(val)] = {
                "category": [["object"] + name.split("::")],
                "attributes": [],
                "labelid": str(uuid4()),
                "dicom": {"instanceid": val},
            }

        for num in range(rb_segmentation.GetNumberOfSegments()):
            seg = rb_segmentation.GetNthSegment(num)
            name = seg.GetName()
            if name not in self.segments and "+" in name:
                sub_instances_names = name.split("+")
                if all(
                    sub_instance_name in labels
                    for sub_instance_name in sub_instances_names
                ):
                    print(f"Adding overlapped label: `{name}`")
                    val = num + 1  # seg.GetLabelValue()
                    for sub_instance_name in sub_instances_names:
                        if not labels[sub_instance_name]["dicom"].get("groupids"):
                            labels[sub_instance_name]["dicom"]["groupids"] = []
                        labels[sub_instance_name]["dicom"]["groupids"].append(val)

        segmentationNode = scene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
        referenceVolumeNode = scene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
        labelmapVolumeNode = scene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
        slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(
            segmentationNode, labelmapVolumeNode, referenceVolumeNode
        )
        new_labels = os.path.join(self.task_dir, "new_labels.nii")
        slicer.util.saveNode(labelmapVolumeNode, new_labels)
        scene.RemoveNode(labelmapVolumeNode.GetDisplayNode().GetColorNode())
        scene.RemoveNode(labelmapVolumeNode)

        img = nb.load(new_labels)
        img.set_data_dtype(np.ubyte)
        data = np.round(img.get_fdata()).astype(np.ubyte)
        means = nb.Nifti1Image(data, header=img.header, affine=img.affine)
        new_labels = os.path.join(self.task_dir, "new_labels_converted.nii")
        nb.save(means, new_labels)
        with open(new_labels, "rb") as file_:
            compressed = gzip.compress(file_.read())

        # self.project.labeling.assign_task(self.stage_name, self.task_id, self.user_id)
        task = {
            "taskId": self.task_id,
            "labelBlob": compressed,
            "draft": not finished,
            "labels": list(labels.values()) + self.other_labels,
        }
        self.project.labeling.put_task(self.stage_name, task)

        if finished:
            scene.Clear(0)
