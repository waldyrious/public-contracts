from main.analysis import Analysis, AnalysisManager

from contracts.analysis.analysis import *


_allAnalysis = [
    Analysis('municipalities_delta_time',
             municipalities_delta_time),
    Analysis('municipalities_contracts_time_series',
             municipalities_contracts_time_series),
    Analysis('excluding_municipalities_contracts_time_series',
             exclude_municipalities_contracts_time_series),
    Analysis('municipalities_categories_ranking',
             get_municipalities_specificity),
    Analysis('municipalities_procedure_types_time_series',
             municipalities_procedure_types_time_series),
    Analysis('procedure_type_time_series', procedure_types_time_series),
    Analysis('contracts_time_series', contracts_price_time_series),
    Analysis('contracts_macro_statistics', get_contracts_macro_statistics),
    Analysis('contracts_price_distribution', get_price_histogram),
    Analysis('ministries_contracts_time_series', ministries_contracts_time_series),
    Analysis('ministries_delta_time', ministries_delta_time),
    Analysis('legislation_application_time_series',
             get_legislation_application_time_series),
    Analysis('entities_values_distribution',
             get_entities_value_histogram),
    Analysis('contracted_lorenz_curve',
             get_lorenz_curve)
]


analysis_manager = AnalysisManager()
for x in _allAnalysis:
    analysis_manager.register(x)
