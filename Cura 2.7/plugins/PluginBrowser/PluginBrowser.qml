import UM 1.1 as UM
import QtQuick 2.2
import QtQuick.Dialogs 1.1
import QtQuick.Window 2.2
import QtQuick.Controls 1.1

UM.Dialog
{
    id: base

    title: catalog.i18nc("@title:window", "Find & Update plugins")
    width: 600
    height: 450
    Item
    {
        anchors.fill: parent
        Item
        {
            id: topBar
            height: childrenRect.height;
            width: parent.width
            Label
            {
                id: introText
                text: catalog.i18nc("@label", "Here you can find a list of Third Party plugins.")
                width: parent.width
                height: 30
            }

            Button
            {
                id: refresh
                text: catalog.i18nc("@action:button", "Refresh")
                onClicked: manager.requestPluginList()
                anchors.right: parent.right
                enabled: !manager.isDownloading
            }
        }
        ScrollView
        {
            width: parent.width
            anchors.top: topBar.bottom
            anchors.bottom: bottomBar.top
            anchors.bottomMargin: UM.Theme.getSize("default_margin").height
            frameVisible: true
            ListView
            {
                id: pluginList
                model: manager.pluginsModel
                anchors.fill: parent

                property var activePlugin
                delegate: pluginDelegate
            }
        }
        Item
        {
            id: bottomBar
            width: parent.width
            height: closeButton.height
            anchors.bottom:parent.bottom
            anchors.left: parent.left
            ProgressBar
            {
                id: progressbar
                anchors.bottom: parent.bottom
                minimumValue: 0;
                maximumValue: 100
                anchors.left:parent.left
                anchors.right: closeButton.left
                anchors.rightMargin: UM.Theme.getSize("default_margin").width
                value: manager.isDownloading ? manager.downloadProgress : 0
            }

            Button
            {
                id: closeButton
                text: catalog.i18nc("@action:button", "Close")
                iconName: "dialog-close"
                onClicked:
                {
                    if (manager.isDownloading)
                    {
                        manager.cancelDownload()
                    }
                    base.close();
                }
                anchors.bottom: parent.bottom
                anchors.right: parent.right
            }
        }

        Item
        {
            SystemPalette { id: palette }
            Component
            {
                id: pluginDelegate
                Rectangle
                {
                    width: pluginList.width;
                    height: texts.height;
                    color: index % 2 ? palette.base : palette.alternateBase
                    Column
                    {
                        id: texts
                        width: parent.width
                        height: childrenRect.height
                        anchors.left: parent.left
                        anchors.leftMargin: UM.Theme.getSize("default_margin").width
                        anchors.right: downloadButton.left
                        anchors.rightMargin: UM.Theme.getSize("default_margin").width
                        Label
                        {
                            text: "<b>" + model.name + "</b> - " + model.author
                            width: contentWidth
                            height: contentHeight +  UM.Theme.getSize("default_margin").height
                            verticalAlignment: Text.AlignVCenter
                        }

                        Label
                        {
                            text: model.short_description
                            width: parent.width
                            height: contentHeight +  UM.Theme.getSize("default_margin").height
                            wrapMode: Text.WordWrap
                            verticalAlignment: Text.AlignVCenter
                        }
                    }
                    Button
                    {
                        id: downloadButton
                        text:
                        {
                            if (manager.isDownloading && pluginList.activePlugin == model)
                            {
                                return catalog.i18nc("@action:button", "Cancel");
                            }
                            else if (model.already_installed)
                            {
                                if (model.can_upgrade)
                                {
                                    return catalog.i18nc("@action:button", "Upgrade");
                                }
                                return catalog.i18nc("@action:button", "Installed");
                            }
                            return catalog.i18nc("@action:button", "Download");
                        }
                        onClicked:
                        {
                            if(!manager.isDownloading)
                            {
                                pluginList.activePlugin = model;
                                manager.downloadAndInstallPlugin(model.file_location);
                            }
                            else
                            {
                                manager.cancelDownload();
                            }
                        }
                        anchors.right: parent.right
                        anchors.rightMargin: UM.Theme.getSize("default_margin").width
                        anchors.verticalCenter: parent.verticalCenter
                        enabled:
                        {
                            if (manager.isDownloading)
                            {
                                return (pluginList.activePlugin == model);
                            }
                            else
                            {
                                return (!model.already_installed || model.can_upgrade);
                            }
                        }
                    }
                }

            }
        }
    UM.I18nCatalog { id: catalog; name:"cura" }
    }
}