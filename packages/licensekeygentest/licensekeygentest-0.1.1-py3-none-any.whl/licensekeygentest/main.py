import machineid
import requests
import json

class library():
  def __init__(self, keygen_account_id, license_key):
    machine_fingerprint = machineid.hashed_id('app-name')
    validation = requests.post(
      f"https://api.keygen.sh/v1/accounts/{keygen_account_id}/licenses/actions/validate-key",
      headers={
        "Content-Type": "application/vnd.api+json",
        "Accept": "application/vnd.api+json"
      },
      data=json.dumps({
        "meta": {
          "scope": { "fingerprint": machine_fingerprint },
          "key": license_key
        }
      })
    ).json()
    if "errors" in validation:
      errs = validation["errors"]
      raise Exception("license validation failed: {}".format(
        map(lambda e: "{} - {}".format(e["title"], e["detail"]).lower(), errs)
      ))

    if validation["meta"]["valid"]:
      print("license has already been activated on this machine")
    
    validation_code = validation["meta"]["code"]
    print(">> Validation Code:", validation_code)
    invalid_code =  validation_code == "SUSPENDED" or \
                    validation_code == "NOT_FOUND"
    
    if invalid_code:
      if validation_code == "SUSPENDED":
        raise Exception("License is suspended. Please contact the library administrator.")
      if validation_code == "NOT_FOUND":
        raise Exception("Invalid License Key. Please recheck license_key")
