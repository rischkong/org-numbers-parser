# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TNArchives.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import numbers_parser.generated.TSPMessages_pb2 as TSPMessages__pb2
import numbers_parser.generated.TSKArchives_pb2 as TSKArchives__pb2
import numbers_parser.generated.TSCHArchives_pb2 as TSCHArchives__pb2
import numbers_parser.generated.TSCEArchives_pb2 as TSCEArchives__pb2
import numbers_parser.generated.TSSArchives_pb2 as TSSArchives__pb2
import numbers_parser.generated.TSDArchives_pb2 as TSDArchives__pb2
import numbers_parser.generated.TSWPArchives_pb2 as TSWPArchives__pb2
import numbers_parser.generated.TSAArchives_pb2 as TSAArchives__pb2
import numbers_parser.generated.TSTArchives_pb2 as TSTArchives__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10TNArchives.proto\x12\x02TN\x1a\x11TSPMessages.proto\x1a\x11TSKArchives.proto\x1a\x12TSCHArchives.proto\x1a\x12TSCEArchives.proto\x1a\x11TSSArchives.proto\x1a\x11TSDArchives.proto\x1a\x12TSWPArchives.proto\x1a\x11TSAArchives.proto\x1a\x11TSTArchives.proto\"\xcd\x03\n\x13SheetUIStateArchive\x12\x12\n\nview_scale\x18\x01 \x02(\x02\x12#\n\x0fscroll_position\x18\x02 \x02(\x0b\x32\n.TSP.Point\x12\x1b\n\x13previous_view_scale\x18\x03 \x01(\x02\x12#\n\x1bscroll_position_is_unscaled\x18\x04 \x01(\x08\x12,\n\x18previous_scroll_position\x18\x05 \x01(\x0b\x32\n.TSP.Point\x12\x1d\n\x15scroll_position_valid\x18\x06 \x01(\x08\x12&\n\x1eprevious_scroll_position_valid\x18\x07 \x01(\x08\x12\x1f\n\x0cvisible_size\x18\x08 \x01(\x0b\x32\t.TSP.Size\x12(\n\x15previous_visible_size\x18\t \x01(\x0b\x32\t.TSP.Size\x12\x14\n\x0c\x64\x65vice_idiom\x18\n \x01(\r\x12\x31\n\x0eselection_path\x18\x0b \x01(\x0b\x32\x19.TSK.SelectionPathArchive\x12\x32\n\x1aselection_path_transformer\x18\x0c \x01(\x0b\x32\x0e.TSP.Reference\"s\n\"SheetUIStateDictionaryEntryArchive\x12\x1d\n\x05sheet\x18\x01 \x02(\x0b\x32\x0e.TSP.Reference\x12.\n\rsheet_uistate\x18\x02 \x02(\x0b\x32\x17.TN.SheetUIStateArchive\"r\n!UUIDSheetUIStateDictionaryArchive\x12\x1d\n\nsheet_uuid\x18\x01 \x02(\x0b\x32\t.TSP.UUID\x12.\n\rsheet_uistate\x18\x02 \x02(\x0b\x32\x17.TN.SheetUIStateArchive\"\x86\x0c\n\x0eUIStateArchive\x12\x1e\n\x12\x61\x63tive_sheet_index\x18\x01 \x02(\rB\x02\x18\x01\x12)\n\rselected_info\x18\x02 \x03(\x0b\x32\x0e.TSP.ReferenceB\x02\x18\x01\x12R\n\x1esheet_uistate_dictionary_entry\x18\x03 \x03(\x0b\x32&.TN.SheetUIStateDictionaryEntryArchiveB\x02\x18\x01\x12\x32\n\x0ftable_selection\x18\x04 \x01(\x0b\x32\x15.TST.SelectionArchiveB\x02\x18\x01\x12\x1f\n\x13\x65\x64iting_sheet_index\x18\x05 \x01(\rB\x02\x18\x01\x12\x15\n\rdocument_mode\x18\x06 \x01(\x05\x12\\\n(edit_mode_sheet_uistate_dictionary_entry\x18\x07 \x03(\x0b\x32&.TN.SheetUIStateDictionaryEntryArchiveB\x02\x18\x01\x12\x1e\n\x12table_editing_mode\x18\x08 \x01(\x05\x42\x02\x18\x01\x12%\n\x19\x66orm_focused_record_index\x18\t \x01(\rB\x02\x18\x01\x12$\n\x18\x66orm_focused_field_index\x18\n \x01(\rB\x02\x18\x01\x12\x15\n\rin_chart_mode\x18\x0b \x01(\x08\x12\x36\n\x0f\x63hart_selection\x18\x0c \x01(\x0b\x32\x19.TN.ChartSelectionArchiveB\x02\x18\x01\x12+\n\x0fsheet_selection\x18\r \x01(\x0b\x32\x0e.TSP.ReferenceB\x02\x18\x01\x12$\n\x16inspector_pane_visible\x18\x0e \x01(\x08:\x04true\x12h\n\x18inspector_pane_view_mode\x18\x0f \x01(\x0e\x32(.TN.UIStateArchive.InspectorPaneViewMode:\x1ckInspectorPaneViewModeFormat\x12%\n\x1dselected_quick_calc_functions\x18\x10 \x03(\r\x12(\n removed_all_quick_calc_functions\x18\x11 \x01(\x08\x12\x1a\n\x12show_canvas_guides\x18\x12 \x01(\x08\x12\x16\n\x0eshows_comments\x18\x13 \x01(\x08\x12)\n\x15\x64\x65sktop_window_origin\x18\x14 \x01(\x0b\x32\n.TSP.Point\x12&\n\x13\x64\x65sktop_window_size\x18\x15 \x01(\x0b\x32\t.TSP.Size\x12&\n\x13\x64\x65sktop_screen_size\x18\x16 \x01(\x0b\x32\t.TSP.Size\x12*\n\x0e\x63hart_ui_state\x18\x17 \x03(\x0b\x32\x12.TSCH.ChartUIState\x12\x31\n\x0eselection_path\x18\x18 \x01(\x0b\x32\x19.TSK.SelectionPathArchive\x12!\n\x19inspector_pane_autohidden\x18\x19 \x01(\x08\x12\x19\n\rshows_sidebar\x18\x1a \x01(\x08\x42\x02\x18\x01\x12\x14\n\x0cshows_rulers\x18\x1b \x01(\x08\x12L\n\x1duuid_sheet_uistate_dictionary\x18\x1c \x03(\x0b\x32%.TN.UUIDSheetUIStateDictionaryArchive\x12\x36\n\x1e\x66reehand_drawing_toolkit_state\x18\x1d \x01(\x0b\x32\x0e.TSP.Reference\x12\x32\n\x1aselection_path_transformer\x18\x1e \x01(\x0b\x32\x0e.TSP.Reference\x12\x18\n\x10\x65\x64iting_disabled\x18\x1f \x01(\x08\x12\x17\n\x0fsidebar_visible\x18  \x01(\x08\x12\x15\n\rsidebar_width\x18! \x01(\x02\"[\n\x15InspectorPaneViewMode\x12 \n\x1ckInspectorPaneViewModeFormat\x10\x00\x12 \n\x1ckInspectorPaneViewModeFilter\x10\x01\"I\n\x15SheetSelectionArchive\x12\x1d\n\x05sheet\x18\x01 \x01(\x0b\x32\x0e.TSP.Reference\x12\x11\n\tpaginated\x18\x02 \x01(\x08\"A\n\x14\x46ormSelectionArchive\x12\x14\n\x0crecord_index\x18\x01 \x02(\r\x12\x13\n\x0b\x66ield_index\x18\x02 \x02(\r\";\n\x1b\x46ormBuilderSelectionArchive\x12\x1c\n\x14viewing_record_index\x18\x01 \x01(\r\"\"\n FormTableChooserSelectionArchive\"<\n\x14UndoRedoStateArchive\x12$\n\x08ui_state\x18\x01 \x02(\x0b\x32\x12.TN.UIStateArchive\"\x89\x03\n\x0f\x44ocumentArchive\x12\x1e\n\x06sheets\x18\x01 \x03(\x0b\x32\x0e.TSP.Reference\x12#\n\x05super\x18\x08 \x02(\x0b\x32\x14.TSA.DocumentArchive\x12.\n\x12\x63\x61lculation_engine\x18\x03 \x01(\x0b\x32\x0e.TSP.ReferenceB\x02\x18\x01\x12\"\n\nstylesheet\x18\x04 \x02(\x0b\x32\x0e.TSP.Reference\x12%\n\rsidebar_order\x18\x05 \x02(\x0b\x32\x0e.TSP.Reference\x12\x1d\n\x05theme\x18\x06 \x02(\x0b\x32\x0e.TSP.Reference\x12#\n\x07uistate\x18\x07 \x01(\x0b\x32\x12.TN.UIStateArchive\x12*\n\x12\x63ustom_format_list\x18\t \x01(\x0b\x32\x0e.TSP.Reference\x12\x16\n\nprinter_id\x18\n \x01(\tB\x02\x18\x01\x12\x10\n\x08paper_id\x18\x0b \x01(\t\x12\x1c\n\tpage_size\x18\x0c \x01(\x0b\x32\t.TSP.Size\";\n\x12PlaceholderArchive\x12%\n\x05super\x18\x01 \x02(\x0b\x32\x16.TSWP.ShapeInfoArchive\"\xbd\x06\n\x0cSheetArchive\x12\x14\n\x04name\x18\x01 \x02(\tB\x06\x92\x82\x19\x02\x08\x05\x12&\n\x0e\x64rawable_infos\x18\x02 \x03(\x0b\x32\x0e.TSP.Reference\x12$\n\x1cin_portrait_page_orientation\x18\x03 \x01(\x08\x12\"\n\x16show_repeating_headers\x18\x04 \x01(\x08\x42\x02\x18\x01\x12\x19\n\x11show_page_numbers\x18\x05 \x01(\x08\x12\x15\n\ris_autofit_on\x18\x06 \x01(\x08\x12\x15\n\rcontent_scale\x18\x07 \x01(\x02\x12!\n\npage_order\x18\x08 \x01(\x0e\x32\r.TN.PageOrder\x12-\n\rprint_margins\x18\n \x01(\x0b\x32\x16.TSD.EdgeInsetsArchive\x12\x1f\n\x17using_start_page_number\x18\x0b \x01(\x08\x12\x19\n\x11start_page_number\x18\x0c \x01(\x05\x12\x19\n\x11page_header_inset\x18\r \x01(\x02\x12\x19\n\x11page_footer_inset\x18\x0e \x01(\x02\x12*\n\x0eheader_storage\x18\x0f \x01(\x0b\x32\x0e.TSP.ReferenceB\x02\x18\x01\x12*\n\x0e\x66ooter_storage\x18\x10 \x01(\x0b\x32\x0e.TSP.ReferenceB\x02\x18\x01\x12/\n\x17userDefinedGuideStorage\x18\x11 \x01(\x0b\x32\x0e.TSP.Reference\x12\x1f\n\x07headers\x18\x12 \x03(\x0b\x32\x0e.TSP.Reference\x12\x1f\n\x07\x66ooters\x18\x13 \x03(\x0b\x32\x0e.TSP.Reference\x12!\n\x19uses_single_header_footer\x18\x14 \x01(\x08\x12Q\n\x10layout_direction\x18\x15 \x01(\x0e\x32\x17.TN.PageLayoutDirection:\x1ePageLayoutDirectionLeftToRight\x12\x1d\n\x05style\x18\x16 \x01(\x0b\x32\x0e.TSP.Reference\x12\x19\n\x11print_backgrounds\x18\x17 \x01(\x08\x12\x1d\n\x15should_print_comments\x18\x18 \x01(\x08\"=\n\x1bSheetStylePropertiesArchive\x12\x1e\n\x04\x66ill\x18\x01 \x01(\x0b\x32\x10.TSD.FillArchive\"\x88\x01\n\x11SheetStyleArchive\x12 \n\x05super\x18\x01 \x02(\x0b\x32\x11.TSS.StyleArchive\x12\x16\n\x0eoverride_count\x18\x02 \x01(\r\x12\x39\n\x10sheet_properties\x18\x03 \x01(\x0b\x32\x1f.TN.SheetStylePropertiesArchive\"^\n\x15\x46ormBasedSheetArchive\x12\x1f\n\x05super\x18\x01 \x02(\x0b\x32\x10.TN.SheetArchive\x12$\n\x08table_id\x18\x02 \x01(\x0b\x32\x12.TSP.CFUUIDArchive\"T\n\x0cThemeArchive\x12 \n\x05super\x18\x01 \x02(\x0b\x32\x11.TSS.ThemeArchive\x12\"\n\nprototypes\x18\x02 \x03(\x0b\x32\x0e.TSP.Reference\"j\n\x1ePasteboardNativeStorageArchive\x12\x1d\n\x05sheet\x18\x01 \x01(\x0b\x32\x0e.TSP.Reference\x12)\n\x08ui_state\x18\x02 \x01(\x0b\x32\x17.TN.SheetUIStateArchive\"\xc7\x03\n\x1b\x43hartMediatorFormulaStorage\x12+\n\rdata_formulae\x18\x01 \x03(\x0b\x32\x14.TSCE.FormulaArchive\x12\x30\n\x12row_label_formulae\x18\x03 \x03(\x0b\x32\x14.TSCE.FormulaArchive\x12\x30\n\x12\x63ol_label_formulae\x18\x04 \x03(\x0b\x32\x14.TSCE.FormulaArchive\x12\x11\n\tdirection\x18\x05 \x01(\x05\x12\x37\n\x19\x65rror_custom_pos_formulae\x18\x06 \x03(\x0b\x32\x14.TSCE.FormulaArchive\x12\x37\n\x19\x65rror_custom_neg_formulae\x18\x07 \x03(\x0b\x32\x14.TSCE.FormulaArchive\x12@\n\"error_custom_pos_scatterX_formulae\x18\x08 \x03(\x0b\x32\x14.TSCE.FormulaArchive\x12@\n\"error_custom_neg_scatterX_formulae\x18\t \x03(\x0b\x32\x14.TSCE.FormulaArchive\x12\x0e\n\x06scheme\x18\n \x01(\x05\"\xcf\x01\n\x14\x43hartMediatorArchive\x12)\n\x05super\x18\x01 \x02(\x0b\x32\x1a.TSCH.ChartMediatorArchive\x12\x11\n\tentity_id\x18\x02 \x02(\t\x12\x31\n\x08\x66ormulas\x18\x03 \x01(\x0b\x32\x1f.TN.ChartMediatorFormulaStorage\x12\x1a\n\x12\x63olumns_are_series\x18\x04 \x01(\x08\x12*\n\x1eis_registered_with_calc_engine\x18\x05 \x01(\x08\x42\x02\x18\x01\"\xcf\x01\n\x15\x43hartSelectionArchive\x12.\n\treference\x18\x01 \x01(\x0b\x32\x1b.TSCE.RangeReferenceArchive\x12\x39\n\x10\x64\x65precated_super\x18\x02 \x01(\x0b\x32\x1b.TSCH.ChartSelectionArchiveB\x02\x18\x01\x12\x1d\n\x05\x63hart\x18\x03 \x01(\x0b\x32\x0e.TSP.Reference\x12,\n\x05super\x18\x04 \x01(\x0b\x32\x1d.TSD.DrawableSelectionArchive\"X\n\"FormCommandActivityBehaviorArchive\x12\x32\n\x05super\x18\x01 \x02(\x0b\x32#.TSK.CommandActivityBehaviorArchive*?\n\tPageOrder\x12\x18\n\x14PageOrderTopToBottom\x10\x00\x12\x18\n\x14PageOrderLeftToRight\x10\x01*]\n\x13PageLayoutDirection\x12\"\n\x1ePageLayoutDirectionLeftToRight\x10\x00\x12\"\n\x1ePageLayoutDirectionRightToLeft\x10\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TNArchives_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _UISTATEARCHIVE.fields_by_name['active_sheet_index']._options = None
  _UISTATEARCHIVE.fields_by_name['active_sheet_index']._serialized_options = b'\030\001'
  _UISTATEARCHIVE.fields_by_name['selected_info']._options = None
  _UISTATEARCHIVE.fields_by_name['selected_info']._serialized_options = b'\030\001'
  _UISTATEARCHIVE.fields_by_name['sheet_uistate_dictionary_entry']._options = None
  _UISTATEARCHIVE.fields_by_name['sheet_uistate_dictionary_entry']._serialized_options = b'\030\001'
  _UISTATEARCHIVE.fields_by_name['table_selection']._options = None
  _UISTATEARCHIVE.fields_by_name['table_selection']._serialized_options = b'\030\001'
  _UISTATEARCHIVE.fields_by_name['editing_sheet_index']._options = None
  _UISTATEARCHIVE.fields_by_name['editing_sheet_index']._serialized_options = b'\030\001'
  _UISTATEARCHIVE.fields_by_name['edit_mode_sheet_uistate_dictionary_entry']._options = None
  _UISTATEARCHIVE.fields_by_name['edit_mode_sheet_uistate_dictionary_entry']._serialized_options = b'\030\001'
  _UISTATEARCHIVE.fields_by_name['table_editing_mode']._options = None
  _UISTATEARCHIVE.fields_by_name['table_editing_mode']._serialized_options = b'\030\001'
  _UISTATEARCHIVE.fields_by_name['form_focused_record_index']._options = None
  _UISTATEARCHIVE.fields_by_name['form_focused_record_index']._serialized_options = b'\030\001'
  _UISTATEARCHIVE.fields_by_name['form_focused_field_index']._options = None
  _UISTATEARCHIVE.fields_by_name['form_focused_field_index']._serialized_options = b'\030\001'
  _UISTATEARCHIVE.fields_by_name['chart_selection']._options = None
  _UISTATEARCHIVE.fields_by_name['chart_selection']._serialized_options = b'\030\001'
  _UISTATEARCHIVE.fields_by_name['sheet_selection']._options = None
  _UISTATEARCHIVE.fields_by_name['sheet_selection']._serialized_options = b'\030\001'
  _UISTATEARCHIVE.fields_by_name['shows_sidebar']._options = None
  _UISTATEARCHIVE.fields_by_name['shows_sidebar']._serialized_options = b'\030\001'
  _DOCUMENTARCHIVE.fields_by_name['calculation_engine']._options = None
  _DOCUMENTARCHIVE.fields_by_name['calculation_engine']._serialized_options = b'\030\001'
  _DOCUMENTARCHIVE.fields_by_name['printer_id']._options = None
  _DOCUMENTARCHIVE.fields_by_name['printer_id']._serialized_options = b'\030\001'
  _SHEETARCHIVE.fields_by_name['name']._options = None
  _SHEETARCHIVE.fields_by_name['name']._serialized_options = b'\222\202\031\002\010\005'
  _SHEETARCHIVE.fields_by_name['show_repeating_headers']._options = None
  _SHEETARCHIVE.fields_by_name['show_repeating_headers']._serialized_options = b'\030\001'
  _SHEETARCHIVE.fields_by_name['header_storage']._options = None
  _SHEETARCHIVE.fields_by_name['header_storage']._serialized_options = b'\030\001'
  _SHEETARCHIVE.fields_by_name['footer_storage']._options = None
  _SHEETARCHIVE.fields_by_name['footer_storage']._serialized_options = b'\030\001'
  _CHARTMEDIATORARCHIVE.fields_by_name['is_registered_with_calc_engine']._options = None
  _CHARTMEDIATORARCHIVE.fields_by_name['is_registered_with_calc_engine']._serialized_options = b'\030\001'
  _CHARTSELECTIONARCHIVE.fields_by_name['deprecated_super']._options = None
  _CHARTSELECTIONARCHIVE.fields_by_name['deprecated_super']._serialized_options = b'\030\001'
  _PAGEORDER._serialized_start=5490
  _PAGEORDER._serialized_end=5553
  _PAGELAYOUTDIRECTION._serialized_start=5555
  _PAGELAYOUTDIRECTION._serialized_end=5648
  _SHEETUISTATEARCHIVE._serialized_start=199
  _SHEETUISTATEARCHIVE._serialized_end=660
  _SHEETUISTATEDICTIONARYENTRYARCHIVE._serialized_start=662
  _SHEETUISTATEDICTIONARYENTRYARCHIVE._serialized_end=777
  _UUIDSHEETUISTATEDICTIONARYARCHIVE._serialized_start=779
  _UUIDSHEETUISTATEDICTIONARYARCHIVE._serialized_end=893
  _UISTATEARCHIVE._serialized_start=896
  _UISTATEARCHIVE._serialized_end=2438
  _UISTATEARCHIVE_INSPECTORPANEVIEWMODE._serialized_start=2347
  _UISTATEARCHIVE_INSPECTORPANEVIEWMODE._serialized_end=2438
  _SHEETSELECTIONARCHIVE._serialized_start=2440
  _SHEETSELECTIONARCHIVE._serialized_end=2513
  _FORMSELECTIONARCHIVE._serialized_start=2515
  _FORMSELECTIONARCHIVE._serialized_end=2580
  _FORMBUILDERSELECTIONARCHIVE._serialized_start=2582
  _FORMBUILDERSELECTIONARCHIVE._serialized_end=2641
  _FORMTABLECHOOSERSELECTIONARCHIVE._serialized_start=2643
  _FORMTABLECHOOSERSELECTIONARCHIVE._serialized_end=2677
  _UNDOREDOSTATEARCHIVE._serialized_start=2679
  _UNDOREDOSTATEARCHIVE._serialized_end=2739
  _DOCUMENTARCHIVE._serialized_start=2742
  _DOCUMENTARCHIVE._serialized_end=3135
  _PLACEHOLDERARCHIVE._serialized_start=3137
  _PLACEHOLDERARCHIVE._serialized_end=3196
  _SHEETARCHIVE._serialized_start=3199
  _SHEETARCHIVE._serialized_end=4028
  _SHEETSTYLEPROPERTIESARCHIVE._serialized_start=4030
  _SHEETSTYLEPROPERTIESARCHIVE._serialized_end=4091
  _SHEETSTYLEARCHIVE._serialized_start=4094
  _SHEETSTYLEARCHIVE._serialized_end=4230
  _FORMBASEDSHEETARCHIVE._serialized_start=4232
  _FORMBASEDSHEETARCHIVE._serialized_end=4326
  _THEMEARCHIVE._serialized_start=4328
  _THEMEARCHIVE._serialized_end=4412
  _PASTEBOARDNATIVESTORAGEARCHIVE._serialized_start=4414
  _PASTEBOARDNATIVESTORAGEARCHIVE._serialized_end=4520
  _CHARTMEDIATORFORMULASTORAGE._serialized_start=4523
  _CHARTMEDIATORFORMULASTORAGE._serialized_end=4978
  _CHARTMEDIATORARCHIVE._serialized_start=4981
  _CHARTMEDIATORARCHIVE._serialized_end=5188
  _CHARTSELECTIONARCHIVE._serialized_start=5191
  _CHARTSELECTIONARCHIVE._serialized_end=5398
  _FORMCOMMANDACTIVITYBEHAVIORARCHIVE._serialized_start=5400
  _FORMCOMMANDACTIVITYBEHAVIORARCHIVE._serialized_end=5488
# @@protoc_insertion_point(module_scope)
