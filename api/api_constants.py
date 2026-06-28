ECFR = 'https://www.ecfr.gov'
# Am I going to end up completely breaking the url up?
SEARCH = '/api/search/v1/results?'
QUERY = 'query='
SPACE = '%20'

# START: Agency slug list
USDA = 'agriculture-department'
EPA = 'environmental-protection-agency'
FDA = 'food-and-drug-administration'
FWS = 'fish-and-wildlife-service'
ATF ='alcohol-tobacco-firearms-and-explosives-bureau'
MMC = 'marine-mammal-commission'

SLUG_ARRAY = [USDA, FDA, EPA, FWS, ATF, MMC] # Updated to constant
# END: Agency slug list


# START: Date parameters
# DATE = 'date='
# LAST_MOD_AFTER = 'last_modified_after='
# LAST_MOD_ON_OR_AFTER = 'last_modified_on_or_after='
# LAST_MOD_BEFORE = 'last_modified_before='
# LAST_MOD_ON_OR_BEFORE = 'last_modified_on_or_before='
# END: Date parameters


# START: Page parameters
PER_PAGE = 'per_page='
PAGE = 'page='
ORDER = 'order='
# Confirm by date returns most recent first.
# NOTE:'date' requires one of the last_modified_* options.
PAGINATE_BY = 'paginate_by='
# END: Page parameters