# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SamplePlugin
                                 A QGIS plugin
 This plugin
                             -------------------
        begin                : 2018-01-16
        copyright            : (C) 2018 by linz
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SamplePlugin class from file SamplePlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sample_plugin import SamplePlugin
    return SamplePlugin(iface)
