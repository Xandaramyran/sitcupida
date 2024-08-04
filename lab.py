from datetime import datetime
import pytz

def convert_time_zone(date, from_time_zone, to_time_zone):
    from_zone = pytz.timezone(from_time_zone)
    to_zone = pytz.timezone(to_time_zone)
    
    # Localize the date to the from_time_zone
    local_date = from_zone.localize(date)
    
    # Convert to the to_time_zone
    converted_date = local_date.astimezone(to_zone)
    return converted_date

date = datetime.now()  # Current date and time
mcmurdo_time_zone = 'Antarctica/McMurdo'
auckland_time_zone = 'Pacific/Auckland'

converted_date = convert_time_zone(date, mcmurdo_time_zone, auckland_time_zone)

print('Original Date:', date)
print('Converted Date:', converted_date)
