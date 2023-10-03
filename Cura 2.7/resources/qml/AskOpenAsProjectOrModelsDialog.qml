// Copyright (c) 2015 Ultimaker B.V.
// Cura is released under the terms of the AGPLv3 or higher.

import QtQuick 2.2
import QtQuick.Controls 1.1
import QtQuick.Controls.Styles 1.1
import QtQuick.Layouts 1.1
import QtQuick.Dialogs 1.1
import QtQuick.Window 2.1

import UM 1.3 as UM
import Cura 1.0 as Cura


UM.Dialog
{
    // This dialog asks the user whether he/she wants to open a project file as a project or import models.
    id: base

    title: catalog.i18nc("@title:window", "Open project file")
    width: 450
    height: 150

    maximumHeight: height
    maximumWidth: width
    minimumHeight: maximumHeight
    minimumWidth: maximumWidth

    modality: UM.Application.platform == "linux" ? Qt.NonModal : Qt.WindowModal;

    property var fileUrl

    function loadProjectFile(projectFile)
    {
        UM.WorkspaceFileHandler.readLocalFile(projectFile);

        var meshName = backgroundItem.getMeshName(projectFile.toString());
        backgroundItem.hasMesh(decodeURIComponent(meshName));
    }

    function loadModelFiles(fileUrls)
    {
        for (var i in fileUrls)
        {
            CuraApplication.readLocalFile(fileUrls[i]);
        }

        var meshName = backgroundItem.getMeshName(fileUrls[0].toString());
        backgroundItem.hasMesh(decodeURIComponent(meshName));
    }

    onVisibleChanged:
    {
        if (visible)
        {
            var rememberMyChoice = UM.Preferences.getValue("cura/choice_on_open_project") != "always_ask";
            rememberChoiceCheckBox.checked = rememberMyChoice;
        }
    }

    Column
    {
        anchors.fill: parent
        anchors.leftMargin: 20
        anchors.rightMargin: 20
        anchors.bottomMargin: 20
        spacing: 10

        Label
        {
            text: catalog.i18nc("@text:window", "This is a Cura project file. Would you like to open it as a project or import the models from it?")
            anchors.left: parent.left
            anchors.right: parent.right
            font: UM.Theme.getFont("default")
            wrapMode: Text.WordWrap
        }

        CheckBox
        {
            id: rememberChoiceCheckBox
            text: catalog.i18nc("@text:window", "Remember my choice")
            checked: UM.Preferences.getValue("cura/choice_on_open_project") != "always_ask"
        }

        // Buttons
        Item
        {
            anchors.right: parent.right
            anchors.left: parent.left
            height: childrenRect.height

            Button
            {
                id: openAsProjectButton
                text: catalog.i18nc("@action:button", "Open as project");
                anchors.right: importModelsButton.left
                anchors.rightMargin: UM.Theme.getSize("default_margin").width
                isDefault: true
                onClicked:
                {
                    // update preference
                    if (rememberChoiceCheckBox.checked)
                        UM.Preferences.setValue("cura/choice_on_open_project", "open_as_project");

                    // load this file as project
                    base.hide();
                    loadProjectFile(base.fileUrl);
                }
            }

            Button
            {
                id: importModelsButton
                text: catalog.i18nc("@action:button", "Import models");
                anchors.right: parent.right
                onClicked:
                {
                    // update preference
                    if (rememberChoiceCheckBox.checked)
                        UM.Preferences.setValue("cura/choice_on_open_project", "open_as_model");

                    // load models from this project file
                    base.hide();
                    loadModelFiles([base.fileUrl]);
                }
            }
        }
    }
}
