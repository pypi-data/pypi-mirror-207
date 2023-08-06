import machineid
import requests
import json
import sys
import os

class library():
  def __init__(self, license_key):
    machine_fingerprint = machineid.hashed_id('example-app')
    validation = requests.post(
      "https://api.keygen.sh/v1/accounts/{}/licenses/actions/validate-key".format(os.environ['KEYGEN_ACCOUNT_ID']),
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
      return False, "license validation failed: {}".format(
        map(lambda e: "{} - {}".format(e["title"], e["detail"]).lower(), errs)
      )

    if validation["meta"]["valid"]:
      return True, "license has already been activated on this machine"
    
    validation_code = validation["meta"]["code"]
    activation_is_required = validation_code == 'FINGERPRINT_SCOPE_MISMATCH' or \
                             validation_code == 'NO_MACHINES' or \
                             validation_code == 'NO_MACHINE'

    if not activation_is_required:
      return False, "license {}".format(validation["meta"]["detail"])

    activation = requests.post(
      "https://api.keygen.sh/v1/accounts/{}/machines".format(os.environ['KEYGEN_ACCOUNT_ID']),
      headers={
        "Authorization": "License {}".format(license_key),
        "Content-Type": "application/vnd.api+json",
        "Accept": "application/vnd.api+json"
      },
      data=json.dumps({
        "data": {
          "type": "machines",
          "attributes": {
            "fingerprint": machine_fingerprint
          },
          "relationships": {
            "license": {
              "data": { "type": "licenses", "id": validation["data"]["id"] }
            }
          }
        }
      })
    ).json()

    if "errors" in activation:
      errs = activation["errors"]
      return False, "license activation failed: {}".format(
        ','.join(map(lambda e: "{} - {}".format(e["title"], e["detail"]).lower(), errs))
      )

    return True, "license activated"