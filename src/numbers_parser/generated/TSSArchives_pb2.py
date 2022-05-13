# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TSSArchives.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import numbers_parser.generated.TSPMessages_pb2 as TSPMessages__pb2
import numbers_parser.generated.TSKArchives_pb2 as TSKArchives__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11TSSArchives.proto\x12\x03TSS\x1a\x11TSPMessages.proto\x1a\x11TSKArchives.proto\"\x97\x01\n\x0cStyleArchive\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10style_identifier\x18\x02 \x01(\t\x12\x1e\n\x06parent\x18\x03 \x01(\x0b\x32\x0e.TSP.Reference\x12\x1b\n\x0cis_variation\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\"\n\nstylesheet\x18\x05 \x01(\x0b\x32\x0e.TSP.Reference\"\xe8\x08\n\x11StylesheetArchive\x12\x1e\n\x06styles\x18\x01 \x03(\x0b\x32\x0e.TSP.Reference\x12L\n\x17identifier_to_style_map\x18\x02 \x03(\x0b\x32+.TSS.StylesheetArchive.IdentifiedStyleEntry\x12\x1e\n\x06parent\x18\x03 \x01(\x0b\x32\x0e.TSP.Reference\x12\x17\n\tis_locked\x18\x04 \x01(\x08:\x04true\x12O\n\x1cparent_to_children_style_map\x18\x05 \x03(\x0b\x32).TSS.StylesheetArchive.StyleChildrenEntry\x12\x1e\n\x0f\x63\x61n_cull_styles\x18\x06 \x01(\x08:\x05\x66\x61lse\x12?\n\x0fstyles_for_10_0\x18\x07 \x01(\x0b\x32&.TSS.StylesheetArchive.VersionedStyles\x12?\n\x0fstyles_for_10_1\x18\x08 \x01(\x0b\x32&.TSS.StylesheetArchive.VersionedStyles\x12?\n\x0fstyles_for_10_2\x18\t \x01(\x0b\x32&.TSS.StylesheetArchive.VersionedStyles\x12?\n\x0fstyles_for_11_0\x18\n \x01(\x0b\x32&.TSS.StylesheetArchive.VersionedStyles\x12?\n\x0fstyles_for_11_1\x18\x0b \x01(\x0b\x32&.TSS.StylesheetArchive.VersionedStyles\x12?\n\x0fstyles_for_11_2\x18\x0c \x01(\x0b\x32&.TSS.StylesheetArchive.VersionedStyles\x12?\n\x0fstyles_for_12_0\x18\r \x01(\x0b\x32&.TSS.StylesheetArchive.VersionedStyles\x1aI\n\x14IdentifiedStyleEntry\x12\x12\n\nidentifier\x18\x01 \x02(\t\x12\x1d\n\x05style\x18\x02 \x02(\x0b\x32\x0e.TSP.Reference\x1aV\n\x12StyleChildrenEntry\x12\x1e\n\x06parent\x18\x01 \x02(\x0b\x32\x0e.TSP.Reference\x12 \n\x08\x63hildren\x18\x02 \x03(\x0b\x32\x0e.TSP.Reference\x1a\xd0\x01\n\x0fVersionedStyles\x12\x1e\n\x06styles\x18\x01 \x03(\x0b\x32\x0e.TSP.Reference\x12L\n\x17identifier_to_style_map\x18\x02 \x03(\x0b\x32+.TSS.StylesheetArchive.IdentifiedStyleEntry\x12O\n\x1cparent_to_children_style_map\x18\x03 \x03(\x0b\x32).TSS.StylesheetArchive.StyleChildrenEntry\"\x99\x02\n\x0cThemeArchive\x12)\n\x11legacy_stylesheet\x18\x01 \x01(\x0b\x32\x0e.TSP.Reference\x12\x18\n\x10theme_identifier\x18\x03 \x01(\t\x12+\n\x13\x64ocument_stylesheet\x18\x04 \x01(\x0b\x32\x0e.TSP.Reference\x12\x34\n!old_uuids_for_preset_replacements\x18\x05 \x03(\x0b\x32\t.TSP.UUID\x12\x34\n!new_uuids_for_preset_replacements\x18\x06 \x03(\x0b\x32\t.TSP.UUID\x12!\n\rcolor_presets\x18\n \x03(\x0b\x32\n.TSP.Color*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\xa6\x01\n\x18\x41pplyThemeCommandArchive\x12\"\n\x05super\x18\x01 \x02(\x0b\x32\x13.TSK.CommandArchive\x12 \n\x08\x63ommands\x18\x02 \x03(\x0b\x32\x0e.TSP.Reference\x12!\n\told_theme\x18\x03 \x01(\x0b\x32\x0e.TSP.Reference\x12!\n\tnew_theme\x18\x04 \x01(\x0b\x32\x0e.TSP.Reference\"c\n\x1d\x41pplyThemeChildCommandArchive\x12\"\n\x05super\x18\x01 \x02(\x0b\x32\x13.TSK.CommandArchive\x12\x1e\n\x06parent\x18\x02 \x01(\x0b\x32\x0e.TSP.Reference\"\xa7\x02\n$StyleUpdatePropertyMapCommandArchive\x12\"\n\x05super\x18\x01 \x02(\x0b\x32\x13.TSK.CommandArchive\x12%\n\rcurrent_style\x18\x02 \x02(\x0b\x32\x0e.TSP.Reference\x12\x33\n\x1bstyle_with_old_property_map\x18\x03 \x01(\x0b\x32\x0e.TSP.Reference\x12\x33\n\x1bstyle_with_new_property_map\x18\x04 \x01(\x0b\x32\x0e.TSP.Reference\x12\"\n\nstyle_diff\x18\x07 \x01(\x0b\x32\x0e.TSP.Reference\x12&\n\x18notify_for_style_clients\x18\x06 \x01(\x08:\x04true\"\x98\x01\n ThemeReplacePresetCommandArchive\x12\"\n\x05super\x18\x01 \x02(\x0b\x32\x13.TSK.CommandArchive\x12\x1e\n\x06preset\x18\x03 \x02(\x0b\x32\x0e.TSP.Reference\x12!\n\toldPreset\x18\x04 \x01(\x0b\x32\x0e.TSP.Reference\x12\r\n\x05index\x18\x05 \x02(\r\"\xb3\x01\n%ThemeReplaceColorPresetCommandArchive\x12\"\n\x05super\x18\x01 \x02(\x0b\x32\x13.TSK.CommandArchive\x12\x1d\n\x05theme\x18\x02 \x02(\x0b\x32\x0e.TSP.Reference\x12\x19\n\x05\x63olor\x18\x03 \x02(\x0b\x32\n.TSP.Color\x12\x1d\n\told_color\x18\x04 \x02(\x0b\x32\n.TSP.Color\x12\r\n\x05index\x18\x05 \x02(\r\"\xd1\x01\n!ThemeAddStylePresetCommandArchive\x12\"\n\x05super\x18\x01 \x02(\x0b\x32\x13.TSK.CommandArchive\x12\x1d\n\x05theme\x18\x02 \x02(\x0b\x32\x0e.TSP.Reference\x12\x1e\n\x06preset\x18\x03 \x02(\x0b\x32\x0e.TSP.Reference\x12\x13\n\x0bpreset_kind\x18\x04 \x02(\t\x12\x12\n\nidentifier\x18\x05 \x01(\t\x12 \n\x18\x61\x64\x64_preset_to_stylesheet\x18\x06 \x01(\x08\"\xf4\x01\n$ThemeRemoveStylePresetCommandArchive\x12\"\n\x05super\x18\x01 \x02(\x0b\x32\x13.TSK.CommandArchive\x12\x1d\n\x05theme\x18\x02 \x02(\x0b\x32\x0e.TSP.Reference\x12\x1e\n\x06preset\x18\x03 \x02(\x0b\x32\x0e.TSP.Reference\x12\x14\n\x0cpreset_index\x18\x04 \x02(\r\x12\x13\n\x0bpreset_kind\x18\x05 \x02(\t\x12\x12\n\nidentifier\x18\x06 \x01(\t\x12*\n\x12replacement_preset\x18\x07 \x01(\x0b\x32\x0e.TSP.Reference\"\xa6\x01\n\x1dThemeMovePresetCommandArchive\x12\"\n\x05super\x18\x01 \x02(\x0b\x32\x13.TSK.CommandArchive\x12\x1d\n\x05theme\x18\x02 \x02(\x0b\x32\x0e.TSP.Reference\x12\x1c\n\tpreset_id\x18\x03 \x02(\x0b\x32\t.TSP.UUID\x12\x11\n\tnew_index\x18\x04 \x02(\r\x12\x11\n\told_index\x18\x05 \x02(\r\"\xaa\x01\n8ThemeReplaceStylePresetAndDisconnectStylesCommandArchive\x12\"\n\x05super\x18\x01 \x02(\x0b\x32\x13.TSK.CommandArchive\x12\x1e\n\x06preset\x18\x02 \x02(\x0b\x32\x0e.TSP.Reference\x12*\n\x12replacement_preset\x18\x03 \x02(\x0b\x32\x0e.TSP.Reference\"\xc3\x01\n\x1b\x43ommandPropertyEntryArchive\x12\x10\n\x08property\x18\x01 \x02(\r\x12\x0c\n\x04type\x18\x02 \x02(\x05\x12\x15\n\rinteger_value\x18\x03 \x01(\x05\x12\x13\n\x0b\x66loat_value\x18\x04 \x01(\x02\x12\x14\n\x0c\x64ouble_value\x18\x05 \x01(\x01\x12\x14\n\x0cstring_value\x18\x06 \x01(\t\x12%\n\rtsp_reference\x18\x07 \x01(\x0b\x32\x0e.TSP.Reference*\x05\x08\x08\x10\xd1\x0f\"W\n\x19\x43ommandPropertyMapArchive\x12:\n\x10property_entries\x18\x01 \x03(\x0b\x32 .TSS.CommandPropertyEntryArchive*G\n\tValueType\x12\x0e\n\nObjectType\x10\x00\x12\x0b\n\x07IntType\x10\x01\x12\r\n\tFloatType\x10\x02\x12\x0e\n\nDoubleType\x10\x03*\xba\x01\n\x0cPropertyType\x12\x17\n\x13InvalidPropertyType\x10\x01\x12\x14\n\x10NullPropertyType\x10\x02\x12\x17\n\x13IntegerPropertyType\x10\x03\x12\x15\n\x11\x46loatPropertyType\x10\x04\x12\x16\n\x12\x44oublePropertyType\x10\x05\x12\x18\n\x14NSStringPropertyType\x10\x06\x12\x19\n\x15TSPObjectPropertyType\x10\x07:;\n\x05\x63olor\x12 .TSS.CommandPropertyEntryArchive\x18\x08 \x01(\x0b\x32\n.TSP.Color')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TSSArchives_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  CommandPropertyEntryArchive.RegisterExtension(color)

  DESCRIPTOR._options = None
  _VALUETYPE._serialized_start=3626
  _VALUETYPE._serialized_end=3697
  _PROPERTYTYPE._serialized_start=3700
  _PROPERTYTYPE._serialized_end=3886
  _STYLEARCHIVE._serialized_start=65
  _STYLEARCHIVE._serialized_end=216
  _STYLESHEETARCHIVE._serialized_start=219
  _STYLESHEETARCHIVE._serialized_end=1347
  _STYLESHEETARCHIVE_IDENTIFIEDSTYLEENTRY._serialized_start=975
  _STYLESHEETARCHIVE_IDENTIFIEDSTYLEENTRY._serialized_end=1048
  _STYLESHEETARCHIVE_STYLECHILDRENENTRY._serialized_start=1050
  _STYLESHEETARCHIVE_STYLECHILDRENENTRY._serialized_end=1136
  _STYLESHEETARCHIVE_VERSIONEDSTYLES._serialized_start=1139
  _STYLESHEETARCHIVE_VERSIONEDSTYLES._serialized_end=1347
  _THEMEARCHIVE._serialized_start=1350
  _THEMEARCHIVE._serialized_end=1631
  _APPLYTHEMECOMMANDARCHIVE._serialized_start=1634
  _APPLYTHEMECOMMANDARCHIVE._serialized_end=1800
  _APPLYTHEMECHILDCOMMANDARCHIVE._serialized_start=1802
  _APPLYTHEMECHILDCOMMANDARCHIVE._serialized_end=1901
  _STYLEUPDATEPROPERTYMAPCOMMANDARCHIVE._serialized_start=1904
  _STYLEUPDATEPROPERTYMAPCOMMANDARCHIVE._serialized_end=2199
  _THEMEREPLACEPRESETCOMMANDARCHIVE._serialized_start=2202
  _THEMEREPLACEPRESETCOMMANDARCHIVE._serialized_end=2354
  _THEMEREPLACECOLORPRESETCOMMANDARCHIVE._serialized_start=2357
  _THEMEREPLACECOLORPRESETCOMMANDARCHIVE._serialized_end=2536
  _THEMEADDSTYLEPRESETCOMMANDARCHIVE._serialized_start=2539
  _THEMEADDSTYLEPRESETCOMMANDARCHIVE._serialized_end=2748
  _THEMEREMOVESTYLEPRESETCOMMANDARCHIVE._serialized_start=2751
  _THEMEREMOVESTYLEPRESETCOMMANDARCHIVE._serialized_end=2995
  _THEMEMOVEPRESETCOMMANDARCHIVE._serialized_start=2998
  _THEMEMOVEPRESETCOMMANDARCHIVE._serialized_end=3164
  _THEMEREPLACESTYLEPRESETANDDISCONNECTSTYLESCOMMANDARCHIVE._serialized_start=3167
  _THEMEREPLACESTYLEPRESETANDDISCONNECTSTYLESCOMMANDARCHIVE._serialized_end=3337
  _COMMANDPROPERTYENTRYARCHIVE._serialized_start=3340
  _COMMANDPROPERTYENTRYARCHIVE._serialized_end=3535
  _COMMANDPROPERTYMAPARCHIVE._serialized_start=3537
  _COMMANDPROPERTYMAPARCHIVE._serialized_end=3624
# @@protoc_insertion_point(module_scope)
