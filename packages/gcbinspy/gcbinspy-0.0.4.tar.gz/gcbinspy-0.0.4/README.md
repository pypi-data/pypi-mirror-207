# gcbinspy

Wrote this to use as a sensor in home assistant so I stop forgetting to take the bins out the night before and inevitably running out in my underwear when the truck wakes me up.

Uses same API https://www.goldcoast.qld.gov.au/Services/Waste-recycling/Find-my-bin-day uses to find your property ID from your address. Alternatively you can manually set your property ID.

Example:

```
import gcbinspy

address = "26 Eleventh Ave, Palm Beach QLD 4221"

client = gcbinspy.GoldCoastBins(address)
client.property_id()
client.update_next_bin_days()
print(client.next_landfill().isoformat())
print(client.is_recycling_day())
print(client.is_organics_day_tomorrow())
```