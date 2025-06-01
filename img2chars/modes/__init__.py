from .mono import MonoMode
from .color import ColorMode
from .edges import EdgesMode
from .edges_cv import EdgesModeCV
from .smart_edges import SmartEdgesMode
from .smart_edges_cv import SmartEdgesModeCV

REGISTERED_MODES = {
    "mono": MonoMode,
    "color": ColorMode,
    "edges": EdgesMode,
    "edges_cv": EdgesModeCV,
    "smart_edges": SmartEdgesMode,
    "smart_edges_cv": SmartEdgesModeCV,
}
