from numbers_parser.generated import TNArchives_pb2 as TNArchives
from numbers_parser.generated import TSTArchives_pb2 as TSTArchives
from numbers_parser.generated import TSCH3DArchives_pb2 as TSCH3DArchives
from numbers_parser.generated import TSSArchives_pb2 as TSSArchives
from numbers_parser.generated import TSAArchives_sos_pb2 as TSAArchives_sos
from numbers_parser.generated import TSCHArchives_GEN_pb2 as TSCHArchives_GEN
from numbers_parser.generated import (
    TSTStylePropertyArchiving_pb2 as TSTStylePropertyArchiving,
)
from numbers_parser.generated import TSPMessages_pb2 as TSPMessages
from numbers_parser.generated import TSDCommandArchives_pb2 as TSDCommandArchives
from numbers_parser.generated import TSCHPreUFFArchives_pb2 as TSCHPreUFFArchives
from numbers_parser.generated import TSWPCommandArchives_pb2 as TSWPCommandArchives
from numbers_parser.generated import TSPDatabaseMessages_pb2 as TSPDatabaseMessages
from numbers_parser.generated import TSSArchives_sos_pb2 as TSSArchives_sos
from numbers_parser.generated import TSDArchives_sos_pb2 as TSDArchives_sos
from numbers_parser.generated import TNCommandArchives_pb2 as TNCommandArchives
from numbers_parser.generated import TSPArchiveMessages_pb2 as TSPArchiveMessages
from numbers_parser.generated import TSCHCommandArchives_pb2 as TSCHCommandArchives
from numbers_parser.generated import TSWPArchives_pb2 as TSWPArchives
from numbers_parser.generated import TSWPArchives_sos_pb2 as TSWPArchives_sos
from numbers_parser.generated import TNCommandArchives_sos_pb2 as TNCommandArchives_sos
from numbers_parser.generated import TSKArchives_sos_pb2 as TSKArchives_sos
from numbers_parser.generated import TSCHArchives_sos_pb2 as TSCHArchives_sos
from numbers_parser.generated import TSDArchives_pb2 as TSDArchives
from numbers_parser.generated import TNArchives_sos_pb2 as TNArchives_sos
from numbers_parser.generated import TSKArchives_pb2 as TSKArchives
from numbers_parser.generated import TSTCommandArchives_pb2 as TSTCommandArchives
from numbers_parser.generated import TSCHArchives_pb2 as TSCHArchives
from numbers_parser.generated import (
    TSACommandArchives_sos_pb2 as TSACommandArchives_sos,
)
from numbers_parser.generated import TSTArchives_sos_pb2 as TSTArchives_sos
from numbers_parser.generated import TSAArchives_pb2 as TSAArchives
from numbers_parser.generated import TSCEArchives_pb2 as TSCEArchives
from numbers_parser.generated import TSCHArchives_Common_pb2 as TSCHArchives_Common


PROTO_FILES = [
    TNArchives,
    TSTArchives,
    TSCH3DArchives,
    TSSArchives,
    TSAArchives_sos,
    TSCHArchives_GEN,
    TSTStylePropertyArchiving,
    TSPMessages,
    TSDCommandArchives,
    TSCHPreUFFArchives,
    TSWPCommandArchives,
    TSPDatabaseMessages,
    TSSArchives_sos,
    TSDArchives_sos,
    TNCommandArchives,
    TSPArchiveMessages,
    TSCHCommandArchives,
    TSWPArchives,
    TSWPArchives_sos,
    TNCommandArchives_sos,
    TSKArchives_sos,
    TSCHArchives_sos,
    TSDArchives,
    TNArchives_sos,
    TSKArchives,
    TSTCommandArchives,
    TSCHArchives,
    TSACommandArchives_sos,
    TSTArchives_sos,
    TSAArchives,
    TSCEArchives,
    TSCHArchives_Common,
]

TSPRegistryMapping = {
    "1": "TN.DocumentArchive",
    "2": "TN.SheetArchive",
    "3": "TN.FormBasedSheetArchive",
    "7": "TN.PlaceholderArchive",
    "200": "TSK.DocumentArchive",
    "201": "TSK.LocalCommandHistory",
    "202": "TSK.CommandGroupArchive",
    "203": "TSK.CommandContainerArchive",
    "205": "TSK.TreeNode",
    "210": "TSK.ViewStateArchive",
    "211": "TSK.DocumentSupportArchive",
    "212": "TSK.AnnotationAuthorArchive",
    "213": "TSK.AnnotationAuthorStorageArchive",
    "215": "TSK.SetAnnotationAuthorColorCommandArchive",
    "218": "TSK.CollaborationCommandHistory",
    "219": "TSK.DocumentSelectionArchive",
    "220": "TSK.CommandSelectionBehaviorArchive",
    "221": "TSK.NullCommandArchive",
    "222": "TSK.CustomFormatListArchive",
    "223": "TSK.GroupCommitCommandArchive",
    "224": "TSK.InducedCommandCollectionArchive",
    "225": "TSK.InducedCommandCollectionCommitCommandArchive",
    "226": "TSK.CollaborationDocumentSessionState",
    "227": "TSK.CollaborationCommandHistoryCoalescingGroup",
    "228": "TSK.CollaborationCommandHistoryCoalescingGroupNode",
    "229": "TSK.CollaborationCommandHistoryOriginatingCommandAcknowledgementObserver",
    "230": "TSK.DocumentSupportCollaborationState",
    "231": "TSK.ChangeDocumentPackageTypeCommandArchive",
    "232": "TSK.UpgradeDocPostProcessingCommandArchive",
    "233": "TSK.FinalCommandPairArchive",
    "234": "TSK.OutgoingCommandQueueItem",
    "235": "TSK.TransformerEntry",
    "238": "TSK.CreateLocalStorageSnapshotCommandArchive",
    "240": "TSK.SelectionPathTransformerArchive",
    "241": "TSK.NativeContentDescription",
    "242": "TSD.PencilAnnotationStorageArchive",
    "245": "TSK.OperationStorage",
    "246": "TSK.OperationStorageEntryArray",
    "247": "TSK.OperationStorageEntryArraySegment",
    "248": "TSK.BlockDiffsAtCurrentRevisionCommand",
    "249": "TSK.OutgoingCommandQueue",
    "250": "TSK.OutgoingCommandQueueSegment",
    "251": "TSK.PropagatedCommandCollectionArchive",
    "252": "TSK.LocalCommandHistoryItem",
    "253": "TSK.LocalCommandHistoryArray",
    "254": "TSK.LocalCommandHistoryArraySegment",
    "255": "TSK.CollaborationCommandHistoryItem",
    "256": "TSK.CollaborationCommandHistoryArray",
    "257": "TSK.CollaborationCommandHistoryArraySegment",
    "258": "TSK.PencilAnnotationUIState",
    "259": "TSKSOS.FixCorruptedDataCommandArchive",
    "260": "TSK.CommandAssetChunkArchive",
    "261": "TSK.AssetUploadStatusCommandArchive",
    "262": "TSK.AssetUnmaterializedOnServerCommandArchive",
    "400": "TSS.StyleArchive",
    "401": "TSS.StylesheetArchive",
    "402": "TSS.ThemeArchive",
    "412": "TSS.StyleUpdatePropertyMapCommandArchive",
    "413": "TSS.ThemeReplacePresetCommandArchive",
    "414": "TSS.ThemeAddStylePresetCommandArchive",
    "415": "TSS.ThemeRemoveStylePresetCommandArchive",
    "416": "TSS.ThemeReplaceColorPresetCommandArchive",
    "417": "TSS.ThemeMovePresetCommandArchive",
    "419": "TSS.ThemeReplaceStylePresetAndDisconnectStylesCommandArchive",
    "600": "TSA.DocumentArchive",
    "601": "TSA.FunctionBrowserStateArchive",
    "602": "TSA.PropagatePresetCommandArchive",
    "603": "TSA.ShortcutControllerArchive",
    "604": "TSA.ShortcutCommandArchive",
    "605": "TSA.AddCustomFormatCommandArchive",
    "606": "TSA.UpdateCustomFormatCommandArchive",
    "607": "TSA.ReplaceCustomFormatCommandArchive",
    "611": "TSASOS.VerifyObjectsWithServerCommandArchive",
    "612": "TSA.InducedVerifyObjectsWithServerCommandArchive",
    "613": "TSASOS.VerifyDocumentWithServerCommandArchive",
    "614": "TSASOS.VerifyDrawableZOrdersWithServerCommandArchive",
    "615": "TSASOS.InducedVerifyDrawableZOrdersWithServerCommandArchive",
    "616": "TSA.NeedsMediaCompatibilityUpgradeCommandArchive",
    "617": "TSA.ChangeDocumentLocaleCommandArchive",
    "618": "TSA.StyleUpdatePropertyMapCommandArchive",
    "619": "TSA.RemoteDataChangeCommandArchive",
    "623": "TSA.GalleryItem",
    "624": "TSA.GallerySelectionTransformer",
    "625": "TSA.GalleryItemSelection",
    "626": "TSA.GalleryItemSelectionTransformer",
    "627": "TSA.GalleryInfoSetValueCommandArchive",
    "628": "TSA.GalleryItemSetGeometryCommand",
    "629": "TSA.GalleryItemSetValueCommand",
    "630": "TSA.InducedVerifyTransformHistoryWithServerCommandArchive",
    "631": "TSASOS.CommandReapplyMasterArchive",
    "632": "TSASOS.PropagateMasterChangeCommandArchive",
    "633": "TSA.CaptionInfoArchive",
    "634": "TSA.CaptionPlacementArchive",
    "635": "TSA.TitlePlacementCommandArchive",
    "636": "TSA.GalleryInfoInsertItemsCommandArchive",
    "637": "TSA.GalleryInfoRemoveItemsCommandArchive",
    "2001": "TSWP.StorageArchive",
    "2002": "TSWP.SelectionArchive",
    "2003": "TSWP.DrawableAttachmentArchive",
    "2004": "TSWP.TextualAttachmentArchive",
    "2005": "TSWP.StorageArchive",
    "2006": "TSWP.UIGraphicalAttachment",
    "2007": "TSWP.TextualAttachmentArchive",
    "2008": "TSWP.FootnoteReferenceAttachmentArchive",
    "2009": "TSWP.TextualAttachmentArchive",
    "2010": "TSWP.TSWPTOCPageNumberAttachmentArchive",
    "2011": "TSWP.ShapeInfoArchive",
    "2013": "TSWP.HighlightArchive",
    "2014": "TSWP.CommentInfoArchive",
    "2015": "TSWP.EquationInfoArchive",
    "2016": "TSWP.PencilAnnotationArchive",
    "2021": "TSWP.CharacterStyleArchive",
    "2022": "TSWP.ParagraphStyleArchive",
    "2023": "TSWP.ListStyleArchive",
    "2024": "TSWP.ColumnStyleArchive",
    "2025": "TSWP.ShapeStyleArchive",
    "2026": "TSWP.TOCEntryStyleArchive",
    "2031": "TSWP.PlaceholderSmartFieldArchive",
    "2032": "TSWP.HyperlinkFieldArchive",
    "2033": "TSWP.FilenameSmartFieldArchive",
    "2034": "TSWP.DateTimeSmartFieldArchive",
    "2035": "TSWP.BookmarkFieldArchive",
    "2036": "TSWP.MergeSmartFieldArchive",
    "2037": "TSWP.CitationRecordArchive",
    "2038": "TSWP.CitationSmartFieldArchive",
    "2039": "TSWP.UnsupportedHyperlinkFieldArchive",
    "2040": "TSWP.BibliographySmartFieldArchive",
    "2041": "TSWP.TOCSmartFieldArchive",
    "2042": "TSWP.RubyFieldArchive",
    "2043": "TSWP.NumberAttachmentArchive",
    "2050": "TSWP.TextStylePresetArchive",
    "2051": "TSWP.TOCSettingsArchive",
    "2052": "TSWP.TOCEntryInstanceArchive",
    "2053": "TSWPSOS.StyleDiffArchive",
    "2060": "TSWP.ChangeArchive",
    "2061": "TSK.DeprecatedChangeAuthorArchive",
    "2062": "TSWP.ChangeSessionArchive",
    "2101": "TSWP.TextCommandArchive",
    "2107": "TSWP.ApplyPlaceholderTextCommandArchive",
    "2116": "TSWP.ApplyRubyTextCommandArchive",
    "2118": "TSWP.ModifyRubyTextCommandArchive",
    "2119": "TSWP.UpdateDateTimeFieldCommandArchive",
    "2120": "TSWP.ModifyTOCSettingsBaseCommandArchive",
    "2121": "TSWP.ModifyTOCSettingsForTOCInfoCommandArchive",
    "2122": "TSWP.ModifyTOCSettingsPresetForThemeCommandArchive",
    "2123": "TSWP.SetObjectPropertiesCommandArchive",
    "2124": "TSWP.UpdateFlowInfoCommandArchive",
    "2125": "TSWP.AddFlowInfoCommandArchive",
    "2126": "TSWP.RemoveFlowInfoCommandArchive",
    "2127": "TSWP.ContainedObjectsCommandArchive",
    "2128": "TSWP.EquationInfoGeometryCommandArchive",
    "2206": "TSWP.AnchorAttachmentCommandArchive",
    "2217": "TSWP.TextCommentReplyCommandArchive",
    "2231": "TSWP.ShapeApplyPresetCommandArchive",
    "2240": "TSWP.TOCInfoArchive",
    "2241": "TSWP.TOCAttachmentArchive",
    "2242": "TSWP.TOCLayoutHintArchive",
    "2400": "TSWP.StyleBaseCommandArchive",
    "2401": "TSWP.StyleCreateCommandArchive",
    "2402": "TSWP.StyleRenameCommandArchive",
    "2404": "TSWP.StyleDeleteCommandArchive",
    "2405": "TSWP.StyleReorderCommandArchive",
    "2406": "TSWP.StyleUpdatePropertyMapCommandArchive",
    "2407": "TSWP.StorageActionCommandArchive",
    "2408": "TSWP.ShapeStyleSetValueCommandArchive",
    "2409": "TSWP.HyperlinkSelectionArchive",
    "2410": "TSWP.FlowInfoArchive",
    "2411": "TSWP.FlowInfoContainerArchive",
    "2412": "TSWP.PencilAnnotationSelectionTransformerArchive",
    "3002": "TSD.DrawableArchive",
    "3003": "TSD.ContainerArchive",
    "3004": "TSD.ShapeArchive",
    "3005": "TSD.ImageArchive",
    "3006": "TSD.MaskArchive",
    "3007": "TSD.MovieArchive",
    "3008": "TSD.GroupArchive",
    "3009": "TSD.ConnectionLineArchive",
    "3015": "TSD.ShapeStyleArchive",
    "3016": "TSD.MediaStyleArchive",
    "3021": "TSD.InfoGeometryCommandArchive",
    "3022": "TSD.DrawablePathSourceCommandArchive",
    "3024": "TSD.ImageMaskCommandArchive",
    "3025": "TSD.ImageMediaCommandArchive",
    "3026": "TSD.ImageReplaceCommandArchive",
    "3027": "TSD.MediaOriginalSizeCommandArchive",
    "3028": "TSD.ShapeStyleSetValueCommandArchive",
    "3030": "TSD.MediaStyleSetValueCommandArchive",
    "3031": "TSD.ShapeApplyPresetCommandArchive",
    "3032": "TSD.MediaApplyPresetCommandArchive",
    "3034": "TSD.MovieSetValueCommandArchive",
    "3036": "TSD.ExteriorTextWrapCommandArchive",
    "3037": "TSD.MediaFlagsCommandArchive",
    "3040": "TSD.DrawableHyperlinkCommandArchive",
    "3041": "TSD.ConnectionLineConnectCommandArchive",
    "3042": "TSD.InstantAlphaCommandArchive",
    "3043": "TSD.DrawableLockCommandArchive",
    "3044": "TSD.ImageNaturalSizeCommandArchive",
    "3045": "TSD.CanvasSelectionArchive",
    "3047": "TSD.GuideStorageArchive",
    "3048": "TSD.StyledInfoSetStyleCommandArchive",
    "3049": "TSD.DrawableInfoCommentCommandArchive",
    "3050": "TSD.GuideCommandArchive",
    "3051": "TSD.DrawableAspectRatioLockedCommandArchive",
    "3052": "TSD.ContainerRemoveChildrenCommandArchive",
    "3053": "TSD.ContainerInsertChildrenCommandArchive",
    "3054": "TSD.ContainerReorderChildrenCommandArchive",
    "3055": "TSD.ImageAdjustmentsCommandArchive",
    "3056": "TSD.CommentStorageArchive",
    "3057": "TSD.ThemeReplaceFillPresetCommandArchive",
    "3058": "TSD.DrawableAccessibilityDescriptionCommandArchive",
    "3059": "TSD.PasteStyleCommandArchive",
    "3061": "TSD.DrawableSelectionArchive",
    "3062": "TSD.GroupSelectionArchive",
    "3063": "TSD.PathSelectionArchive",
    "3064": "TSD.CommentInvalidatingCommandSelectionBehaviorArchive",
    "3065": "TSD.ImageInfoAbstractGeometryCommandArchive",
    "3066": "TSD.ImageInfoGeometryCommandArchive",
    "3067": "TSD.ImageInfoMaskGeometryCommandArchive",
    "3068": "TSD.UndoObjectArchive",
    "3070": "TSD.ReplaceAnnotationAuthorCommandArchive",
    "3071": "TSD.DrawableSelectionTransformerArchive",
    "3072": "TSD.GroupSelectionTransformerArchive",
    "3073": "TSD.ShapeSelectionTransformerArchive",
    "3074": "TSD.PathSelectionTransformerArchive",
    "3080": "TSD.MediaInfoGeometryCommandArchive",
    "3082": "TSD.GroupUngroupInformativeCommandArchive",
    "3083": "TSD.DrawableContentDescription",
    "3084": "TSD.ContainerRemoveDrawablesCommandArchive",
    "3085": "TSD.ContainerInsertDrawablesCommandArchive",
    "3086": "TSD.PencilAnnotationArchive",
    "3087": "TSD.FreehandDrawingOpacityCommandArchive",
    "3088": "TSD.DrawablePencilAnnotationCommandArchive",
    "3089": "TSD.PencilAnnotationSelectionArchive",
    "3090": "TSD.FreehandDrawingContentDescription",
    "3091": "TSD.FreehandDrawingToolkitUIState",
    "3092": "TSD.PencilAnnotationSelectionTransformerArchive",
    "3094": "TSD.FreehandDrawingAnimationCommandArchive",
    "3095": "TSD.InsertCaptionOrTitleCommandArchive",
    "3096": "TSD.RemoveCaptionOrTitleCommandArchive",
    "3097": "TSD.StandinCaptionArchive",
    "3098": "TSD.SetCaptionOrTitleVisibilityCommandArchive",
    "4000": "TSCE.CalculationEngineArchive",
    "4001": "TSCE.FormulaRewriteCommandArchive",
    "4003": "TSCE.NamedReferenceManagerArchive",
    "4004": "TSCE.TrackedReferenceStoreArchive",
    "4005": "TSCE.TrackedReferenceArchive",
    "4007": "TSCE.RemoteDataStoreArchive",
    "4008": "TSCE.FormulaOwnerDependenciesArchive",
    "4009": "TSCE.CellRecordTileArchive",
    "4010": "TSCE.RangePrecedentsTileArchive",
    "4011": "TSCE.ReferencesToDirtyArchive",
    "5000": "TSCH.PreUFF.ChartInfoArchive",
    "5002": "TSCH.PreUFF.ChartGridArchive",
    "5004": "TSCH.ChartMediatorArchive",
    "5010": "TSCH.PreUFF.ChartStyleArchive",
    "5011": "TSCH.PreUFF.ChartSeriesStyleArchive",
    "5012": "TSCH.PreUFF.ChartAxisStyleArchive",
    "5013": "TSCH.PreUFF.LegendStyleArchive",
    "5014": "TSCH.PreUFF.ChartNonStyleArchive",
    "5015": "TSCH.PreUFF.ChartSeriesNonStyleArchive",
    "5016": "TSCH.PreUFF.ChartAxisNonStyleArchive",
    "5017": "TSCH.PreUFF.LegendNonStyleArchive",
    "5020": "TSCH.ChartStylePreset",
    "5021": "TSCH.ChartDrawableArchive",
    "5022": "TSCH.ChartStyleArchive",
    "5023": "TSCH.ChartNonStyleArchive",
    "5024": "TSCH.LegendStyleArchive",
    "5025": "TSCH.LegendNonStyleArchive",
    "5026": "TSCH.ChartAxisStyleArchive",
    "5027": "TSCH.ChartAxisNonStyleArchive",
    "5028": "TSCH.ChartSeriesStyleArchive",
    "5029": "TSCH.ChartSeriesNonStyleArchive",
    "5030": "TSCH.ReferenceLineStyleArchive",
    "5031": "TSCH.ReferenceLineNonStyleArchive",
    "5103": "TSCH.CommandSetChartTypeArchive",
    "5104": "TSCH.CommandSetSeriesNameArchive",
    "5105": "TSCH.CommandSetCategoryNameArchive",
    "5107": "TSCH.CommandSetScatterFormatArchive",
    "5108": "TSCH.CommandSetLegendFrameArchive",
    "5109": "TSCH.CommandSetGridValueArchive",
    "5110": "TSCH.CommandSetGridDirectionArchive",
    "5115": "TSCH.CommandAddGridRowsArchive",
    "5116": "TSCH.CommandAddGridColumnsArchive",
    "5118": "TSCH.CommandMoveGridRowsArchive",
    "5119": "TSCH.CommandMoveGridColumnsArchive",
    "5122": "TSCH.CommandSetPieWedgeExplosion",
    "5123": "TSCH.CommandStyleSwapArchive",
    "5125": "TSCH.CommandChartApplyPreset",
    "5126": "TSCH.ChartCommandArchive",
    "5127": "TSCH.CommandReplaceGridValuesArchive",
    "5129": "TSCH.StylePasteboardDataArchive",
    "5130": "TSCH.CommandSetMultiDataSetIndexArchive",
    "5131": "TSCH.CommandReplaceThemePresetArchive",
    "5132": "TSCH.CommandInvalidateWPCaches",
    "5135": "TSCH.CommandMutatePropertiesArchive",
    "5136": "TSCH.CommandScaleAllTextArchive",
    "5137": "TSCH.CommandSetFontFamilyArchive",
    "5138": "TSCH.CommandApplyFillSetArchive",
    "5139": "TSCH.CommandReplaceCustomFormatArchive",
    "5140": "TSCH.CommandAddReferenceLineArchive",
    "5141": "TSCH.CommandDeleteReferenceLineArchive",
    "5142": "TSCH.CommandDeleteGridColumnsArchive",
    "5143": "TSCH.CommandDeleteGridRowsArchive",
    "5145": "TSCH.ChartSelectionArchive",
    "5146": "TSCH.ChartTextSelectionTransformerArchive",
    "5147": "TSCH.ChartSubselectionTransformerArchive",
    "5148": "TSCH.ChartDrawableSelectionTransformerArchive",
    "5149": "TSCH.ChartSubselectionTransformerHelperArchive",
    "5150": "TSCH.ChartRefLineSubselectionTransformerHelperArchive",
    "5151": "TSCH.CDESelectionTransformerArchive",
    "5152": "TSCH.ChartSubselectionIdentityTransformerHelperArchive",
    "5154": "TSCH.CommandPasteStyleArchive",
    "5155": "TSCH.CommandInducedReplaceChartGrid",
    "5156": "TSCH.CommandReplaceImageDataArchive",
    "5157": "TSCH.CommandInduced3DChartGeometry",
    "6000": "TST.TableInfoArchive",
    "6001": "TST.TableModelArchive",
    "6002": "TST.Tile",
    "6003": "TST.TableStyleArchive",
    "6004": "TST.CellStyleArchive",
    "6005": "TST.TableDataList",
    "6006": "TST.HeaderStorageBucket",
    "6007": "TST.WPTableInfoArchive",
    "6008": "TST.TableStylePresetArchive",
    "6009": "TST.TableStrokePresetArchive",
    "6010": "TST.ConditionalStyleSetArchive",
    "6011": "TST.TableDataListSegment",
    "6030": "TST.SelectionArchive",
    "6031": "TST.CellMapArchive",
    "6032": "TST.DeathhawkRdar39989167CellSelectionArchive",
    "6033": "TST.ConcurrentCellMapArchive",
    "6034": "TST.ConcurrentCellListArchive",
    "6100": "TST.TableCommandArchive",
    "6101": "TST.CommandDeleteCellsArchive",
    "6102": "TST.CommandInsertColumnsOrRowsArchive",
    "6103": "TST.CommandRemoveColumnsOrRowsArchive",
    "6104": "TST.CommandResizeColumnOrRowArchive",
    "6107": "TST.CommandSetTableNameArchive",
    "6111": "TST.CommandChangeFreezeHeaderStateArchive",
    "6114": "TST.CommandSetTableNameEnabledArchive",
    "6117": "TST.CommandApplyTableStylePresetArchive",
    "6120": "TST.CommandSetRepeatingHeaderEnabledArchive",
    "6123": "TST.CommandSortArchive",
    "6125": "TST.CommandStyleTableArchive",
    "6126": "TST.CommandSetNumberOfDecimalPlacesArchive",
    "6127": "TST.CommandSetShowThousandsSeparatorArchive",
    "6128": "TST.CommandSetNegativeNumberStyleArchive",
    "6129": "TST.CommandSetFractionAccuracyArchive",
    "6131": "TST.CommandSetCurrencyCodeArchive",
    "6132": "TST.CommandSetUseAccountingStyleArchive",
    "6136": "TST.CommandSetTableFontNameArchive",
    "6137": "TST.CommandSetTableFontSizeArchive",
    "6142": "TST.CommandSetTableNameHeightArchive",
    "6144": "TST.MergeRegionMapArchive",
    "6145": "TST.CommandHideShowArchive",
    "6146": "TST.CommandSetBaseArchive",
    "6147": "TST.CommandSetBasePlacesArchive",
    "6148": "TST.CommandSetBaseUseMinusSignArchive",
    "6149": "TST.CommandSetTextStylePropertiesArchive",
    "6150": "TST.CommandCategoryChangeSummaryAggregateType",
    "6152": "TST.CommandCategoryResizeColumnOrRowArchive",
    "6153": "TST.CommandCategoryMoveRowsArchive",
    "6156": "TST.CommandSetPencilAnnotationsArchive",
    "6157": "TST.CommandCategoryWillChangeGroupValue",
    "6158": "TST.CommandApplyConcurrentCellMapArchive",
    "6159": "TST.CommandSetGroupSortOrderArchive",
    "6179": "TST.FormulaEqualsTokenAttachmentArchive",
    "6181": "TST.TokenAttachmentArchive",
    "6182": "TST.ExpressionNodeArchive",
    "6183": "TST.BooleanNodeArchive",
    "6184": "TST.NumberNodeArchive",
    "6185": "TST.StringNodeArchive",
    "6186": "TST.ArrayNodeArchive",
    "6187": "TST.ListNodeArchive",
    "6188": "TST.OperatorNodeArchive",
    "6189": "TST.FunctionNodeArchive",
    "6190": "TST.DateNodeArchive",
    "6191": "TST.ReferenceNodeArchive",
    "6192": "TST.DurationNodeArchive",
    "6193": "TST.ArgumentPlaceholderNodeArchive",
    "6194": "TST.PostfixOperatorNodeArchive",
    "6195": "TST.PrefixOperatorNodeArchive",
    "6196": "TST.FunctionEndNodeArchive",
    "6197": "TST.EmptyExpressionNodeArchive",
    "6198": "TST.LayoutHintArchive",
    "6199": "TST.CompletionTokenAttachmentArchive",
    "6201": "TST.TableDataList",
    "6204": "TST.HiddenStateFormulaOwnerArchive",
    "6205": "TST.CommandSetAutomaticDurationUnitsArchive",
    "6206": "TST.PopUpMenuModel",
    "6218": "TST.RichTextPayloadArchive",
    "6220": "TST.FilterSetArchive",
    "6221": "TST.CommandSetFiltersEnabledArchive",
    "6224": "TST.CommandRewriteFilterFormulasForTableResizeArchive",
    "6226": "TST.CommandTextPreflightInsertCellArchive",
    "6228": "TST.CommandDeleteCellContentsArchive",
    "6229": "TST.CommandPostflightSetCellArchive",
    "6235": "TST.IdentifierNodeArchive",
    "6238": "TST.CommandSetDateTimeFormatArchive",
    "6239": "TST.TableCommandSelectionBehaviorArchive",
    "6244": "TST.CommandApplyCellCommentArchive",
    "6246": "TST.CommandSetFormulaTokenizationArchive",
    "6247": "TST.TableStyleNetworkArchive",
    "6250": "TST.CommandSetFilterSetTypeArchive",
    "6255": "TST.CommandSetTextStyleArchive",
    "6256": "TST.CommandJustForNotifyingArchive",
    "6258": "TST.CommandSetSortOrderArchive",
    "6262": "TST.CommandAddTableStylePresetArchive",
    "6264": "TST.CellDiffMapArchive",
    "6265": "TST.CommandApplyCellContentsArchive",
    "6266": "TST.CommandRemoveTableStylePresetArchive",
    "6267": "TST.ColumnRowUIDMapArchive",
    "6268": "TST.CommandMoveColumnsOrRowsArchive",
    "6269": "TST.CommandReplaceCustomFormatArchive",
    "6270": "TST.CommandReplaceTableStylePresetArchive",
    "6271": "TST.FormulaSelectionArchive",
    "6273": "TST.CellListArchive",
    "6275": "TST.CommandApplyCellDiffMapArchive",
    "6276": "TST.CommandSetFilterSetArchive",
    "6277": "TST.CommandMutateCellFormatArchive",
    "6278": "TST.CommandSetStorageLanguageArchive",
    "6280": "TST.CommandMergeArchive",
    "6281": "TST.CommandUnmergeArchive",
    "6282": "TST.CommandApplyCellMapArchive",
    "6283": "TST.ControlCellSelectionArchive",
    "6284": "TST.TableNameSelectionArchive",
    "6285": "TST.CommandRewriteFormulasForTransposeArchive",
    "6287": "TST.CommandTransposeTableArchive",
    "6289": "TST.CommandSetDurationStyleArchive",
    "6290": "TST.CommandSetDurationUnitSmallestLargestArchive",
    "6291": "TST.CommandRewriteTableFormulasForRewriteSpecArchive",
    "6292": "TST.CommandRewriteConditionalStylesForRewriteSpecArchive",
    "6293": "TST.CommandRewriteFilterFormulasForRewriteSpecArchive",
    "6294": "TST.CommandRewriteSortOrderForRewriteSpecArchive",
    "6295": "TST.StrokeSelectionArchive",
    "6297": "TST.LetNodeArchive",
    "6298": "TST.VariableNodeArchive",
    "6299": "TST.InNodeArchive",
    "6300": "TST.CommandInverseMergeArchive",
    "6301": "TST.CommandMoveCellsArchive",
    "6302": "TST.DefaultCellStylesContainerArchive",
    "6303": "TST.CommandRewriteMergeFormulasArchive",
    "6304": "TST.CommandChangeTableAreaForColumnOrRowArchive",
    "6305": "TST.StrokeSidecarArchive",
    "6306": "TST.StrokeLayerArchive",
    "6307": "TST.CommandChooseTableIdRemapperArchive",
    "6310": "TST.CommandSetWasCutArchive",
    "6311": "TST.AutofillSelectionArchive",
    "6312": "TST.StockCellSelectionArchive",
    "6313": "TST.CommandSetNowArchive",
    "6314": "TST.CommandSetStructuredTextImportRecordArchive",
    "6315": "TST.CommandRewriteCategoryFormulasArchive",
    "6316": "TST.SummaryModelArchive",
    "6317": "TST.SummaryCellVendorArchive",
    "6318": "TST.CategoryOrderArchive",
    "6320": "TST.CommandCategoryCollapseExpandGroupArchive",
    "6321": "TST.CommandCategorySetGroupingColumnsArchive",
    "6323": "TST.CommandRewriteHiddenStatesForGroupByChangeArchive",
    "6350": "TST.IdempotentSelectionTransformerArchive",
    "6351": "TST.TableSubSelectionTransformerBaseArchive",
    "6352": "TST.TableNameSelectionTransformerArchive",
    "6353": "TST.RegionSelectionTransformerArchive",
    "6354": "TST.RowColumnSelectionTransformerArchive",
    "6355": "TST.ControlCellSelectionTransformerArchive",
    "6357": "TST.ChangePropagationMapWrapper",
    "6358": "TST.WPSelectionTransformerArchive",
    "6359": "TST.StockCellSelectionTransformerArchive",
    "6360": "TST.CommandSetRangeControlMinMaxIncArchive",
    "6361": "TST.CommandCategorySetLabelRowVisibility",
    "6362": "TST.CommandRewritePencilAnnotationFormulasArchive",
    "6363": "TST.PencilAnnotationArchive",
    "6364": "TST.StrokeSelectionTransformerArchive",
    "6365": "TST.HeaderNameMgrTileArchive",
    "6366": "TST.HeaderNameMgrArchive",
    "6367": "TST.CellDiffArray",
    "6368": "TST.CellDiffArraySegment",
    "6369": "TST.PivotOrderArchive",
    "6370": "TST.PivotOwnerArchive",
    "6371": "TST.CommandPivotSetPivotRulesArchive",
    "6372": "TST.CategoryOwnerRefArchive",
    "6373": "TST.GroupByArchive",
    "6374": "TST.PivotGroupingColumnOptionsMapArchive",
    "6375": "TST.CommandPivotSetGroupingColumnOptionsArchive",
    "6376": "TST.CommandPivotHideShowGrandTotalsArchive",
    "6377": "TST.CommandPivotSortArchive",
    "6379": "TST.CommandRewritePivotOwnerFormulasArchive",
    "6380": "TST.CommandRewriteTrackedReferencesArchive",
    "6381": "TST.CommandExtendTableIDHistoryArchive",
    "6382": "TST.GroupByArchive.AggregatorArchive",
    "6383": "TST.GroupByArchive.GroupNodeArchive",
    "10011": "TSWP.SectionPlaceholderArchive",
    "10020": "TSWP.ShapeSelectionTransformerArchive",
    "10021": "TSWP.SelectionTransformerArchive",
    "10022": "TSWP.ShapeContentDescription",
    "10023": "TSWP.TateChuYokoFieldArchive",
    "10024": "TSWP.DropCapStyleArchive",
    "11000": "TSP.PasteboardObject",
    "11006": "TSP.PackageMetadata",
    "11007": "TSP.PasteboardMetadata",
    "11008": "TSP.ObjectContainer",
    "11009": "TSP.ViewStateMetadata",
    "11010": "TSP.ObjectCollection",
    "11011": "TSP.DocumentMetadata",
    "11012": "TSP.SupportMetadata",
    "11013": "TSP.ObjectSerializationMetadata",
    "11014": "TSP.DataMetadata",
    "11015": "TSP.DataMetadataMap",
    "11016": "TSP.LargeNumberArraySegment",
    "11017": "TSP.LargeStringArraySegment",
    "11018": "TSP.LargeLazyObjectArraySegment",
    "11019": "TSP.LargeNumberArray",
    "11020": "TSP.LargeStringArray",
    "11021": "TSP.LargeLazyObjectArray",
    "11024": "TSP.LargeUUIDArraySegment",
    "11025": "TSP.LargeUUIDArray",
    "11026": "TSP.LargeObjectArraySegment",
    "11027": "TSP.LargeObjectArray",
    "12002": "TN.CommandSheetInsertDrawablesArchive",
    "12003": "TN.CommandDocumentInsertSheetArchive",
    "12004": "TN.CommandDocumentRemoveSheetArchive",
    "12005": "TN.CommandSetSheetNameArchive",
    "12006": "TN.ChartMediatorArchive",
    "12008": "TN.CommandDocumentReorderSheetArchive",
    "12009": "TN.ThemeArchive",
    "12012": "TN.CommandSheetRemoveDrawablesArchive",
    "12013": "TN.CommandSheetMoveDrawableZOrderArchive",
    "12014": "TN.CommandChartMediatorSetEditingState",
    "12015": "TN.CommandFormChooseTargetTableArchive",
    "12017": "TN.CommandSetPageOrientationArchive",
    "12018": "TN.CommandSetContentScaleArchive",
    "12026": "TN.UIStateArchive",
    "12028": "TN.SheetSelectionArchive",
    "12030": "TN.CommandSetDocumentPaperSize",
    "12031": "TN.CommandSetPrinterMarginsArchive",
    "12032": "TN.CommandSetHeaderFooterInsetsArchive",
    "12033": "TN.CommandSetPageOrderArchive",
    "12034": "TN.CommandSetUsingStartPageNumberArchive",
    "12035": "TN.CommandSetStartPageNumberArchive",
    "12036": "TN.ChartSelectionArchive",
    "12037": "TN.CommandChartMediatorSetGridDirection",
    "12038": "TN.CommandChartMediatorSetFormula",
    "12039": "TN.CommandChartMediatorSetSeriesOrder",
    "12040": "TN.FormSelectionArchive",
    "12041": "TN.DocumentSelectionTransformerArchive",
    "12042": "TN.SheetSelectionTransformerArchive",
    "12043": "TN.CommandInducedSheetChangeArchive",
    "12044": "TNSOS.InducedVerifyDocumentWithServerCommandArchive",
    "12045": "TNSOS.InducedVerifyDrawableZOrdersWithServerCommandArchive",
    "12046": "TN.PasteboardNativeStorageArchive",
    "12047": "TN.CanvasSelectionTransformerArchive",
    "12048": "TN.CommandSetSheetDirectionArchive",
    "12049": "TN.CommandSetSheetShouldPrintCommentsArchive",
    "12050": "TN.SheetStyleArchive",
    "12051": "TN.CommandSheetSetBackgroundFillArchive",
    "12052": "TN.CommandSetPrintBackgroundsArchive",
    "12053": "TN.FormBuilderSelectionArchive",
    "12054": "TN.FormTableChooserSelectionArchive",
    "12055": "TN.FormTableChooserSelectionTransformerArchive",
    "12056": "TN.FormBuilderSelectionTransformerArchive",
    "12057": "TN.FormViewerSelectionTransformerArchive",
    "12058": "TN.FormSheetSelectionTransformerArchive",
}


def compute_maps():
    name_class_map = {}

    def add_nested_types(message_type):
        for name in dict(message_type.DESCRIPTOR.nested_types_by_name):
            child_type = getattr(message_type, name)
            name_class_map[child_type.DESCRIPTOR.full_name] = child_type
            add_nested_types(child_type)

    for file in PROTO_FILES:
        for message_name in dict(file.DESCRIPTOR.message_types_by_name):
            message_type = getattr(file, message_name)
            name_class_map[message_type.DESCRIPTOR.full_name] = message_type
            add_nested_types(message_type)

    id_name_map = {}
    name_id_map = {}
    for k, v in list(TSPRegistryMapping.items()):
        if v in name_class_map:
            id_name_map[int(k)] = name_class_map[v]
            name_id_map[v] = int(k)

    return name_class_map, id_name_map, name_id_map


NAME_CLASS_MAP, ID_NAME_MAP, NAME_ID_MAP = compute_maps()
