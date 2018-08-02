# Sessions

{% api-method method="get" host="https://api.streamelements.com" path="/kappa/v2/sessions/:channel" %}
  {% api-method-summary %}
    Get session
  {% endapi-method-summary %}

  {% api-method-description %}
    This endpoint allows you to get the active stream session.
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="channel" type="string" required=true %}
          The channelId
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}

      {% api-method-headers %}
        {% api-method-parameter name="Authorization" type="string" required=true %}
          The Bearer token
        {% endapi-method-parameter %}
      {% endapi-method-headers %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}
          Session successfully retrieved.
        {% endapi-method-response-example-description %}

        ```javascript
        {
        "_id": "5af42bb472b82a8690e3423b",
        "provider": "twitch",
        "lastReset": "2018-05-10T11:23:32.891Z",
        "channel": "577c0455f9a31ea72a36b2b3",
        "createdAt": "2018-05-10T11:23:32.914Z",
        "updatedAt": "2018-05-10T11:24:04.128Z",
        "data": {
        "follower-latest": {
            "name": "xd"
        },
        "follower-session": {
            "count": 2
        },
        "follower-week": {
            "count": 2
        },
        "follower-month": {
            "count": 2
        },
        "follower-goal": {
            "amount": 18
        },
        "follower-total": {
            "count": 49
        },
        "subscriber-latest": {
            "name": "",
            "amount": 0,
            "tier": "",
            "message": ""
        },
        "subscriber-session": {
            "count": 0
        },
        "subscriber-week": {
            "count": 0
        },
        "subscriber-month": {
            "count": 0
        },
        "subscriber-goal": {
            "amount": 0
        },
        "subscriber-total": {
            "count": 0
        },
        "subscriber-points": {
            "amount": 0
        },
        "host-latest": {
            "name": "",
            "amount": 0
        },
        "raid-latest": {
            "name": "",
            "amount": 0
        },
        "cheer-session": {
            "amount": 0
        },
        "cheer-week": {
            "amount": 0
        },
        "cheer-month": {
            "amount": 0
        },
        "cheer-total": {
            "amount": 496
        },
        "cheer-count": {
            "count": 0
        },
        "cheer-goal": {
            "amount": 0
        },
        "cheer-latest": {
            "name": "",
            "amount": 0,
            "message": ""
        },
        "cheer-session-top-donation": {
            "name": "",
            "amount": 0
        },
        "cheer-weekly-top-donation": {
            "name": "",
            "amount": 0
        },
        "cheer-monthly-top-donation": {
            "name": "",
            "amount": 0
        },
        "cheer-alltime-top-donation": {
            "name": "telekinesis_360",
            "amount": 122
        },
        "cheer-session-top-donator": {
            "name": "",
            "amount": 0
        },
        "cheer-weekly-top-donator": {
            "name": "",
            "amount": 0
        },
        "cheer-monthly-top-donator": {
            "name": "",
            "amount": 0
        },
        "cheer-alltime-top-donator": {
            "name": "xdxd_ross",
            "amount": 200
        },
        "tip-latest": {
            "name": "rhaegal_meh",
            "amount": 5,
            "message": "I’m not that rich but happy to tip for the great work you do on discord server"
        },
        "tip-session-top-donation": {
            "name": "",
            "amount": 0
        },
        "tip-weekly-top-donation": {
            "name": "rhaegal_meh",
            "amount": 5
        },
        "tip-monthly-top-donation": {
            "name": "xd",
            "amount": 5
        },
        "tip-alltime-top-donation": {
            "name": "m0nsterog",
            "amount": 500
        },
        "tip-session-top-donator": {
            "name": "",
            "amount": 0
        },
        "tip-weekly-top-donator": {
            "name": "rhaegal_meh",
            "amount": 5
        },
        "tip-monthly-top-donator": {
            "name": "xd",
            "amount": 35
        },
        "tip-alltime-top-donator": {
            "name": "xd",
            "amount": 2745
        },
        "tip-session": {
            "amount": 0
        },
        "tip-week": {
            "amount": 5
        },
        "tip-month": {
            "amount": 46.5
        },
        "tip-total": {
            "amount": 10139.1255709
        },
        "tip-count": {
            "count": 0
        },
        "tip-goal": {
            "amount": 5859.600000000002
        },
        "follower-recent": [
            {
                "name": "xd",
                "createdAt": "2018-05-10T11:24:04.127Z"
            }
        ],
        "subscriber-recent": [],
        "host-recent": [],
        "raid-recent": [],
        "cheer-recent": [],
        "tip-recent": [
            {
                "name": "rhaegal_meh",
                "amount": 5,
                "createdAt": "2018-05-09T14:13:59.191Z"
            }
        ]
        }
        }
        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=401 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```javascript
        "statusCode": 401,
        "error": "Unauthorized",
        "message": "No authorization token was found"
        }
        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

{% api-method method="put" host="https://api.streamelements.com" path="/kappa/v2/sessions/:channel" %}
  {% api-method-summary %}
    Update a session
  {% endapi-method-summary %}

  {% api-method-description %}

  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="" type="string" required=false %}

        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

{% api-method method="put" host="https://api.streamelements.com" path="/kappa/v2/sessions/:channel" %}
  {% api-method-summary %}
    Reset a session
  {% endapi-method-summary %}

  {% api-method-description %}
    Resetting a session will create a brand new session.  
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="" type="string" required=false %}

        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

{% api-method method="put" host="https://api.streamelements.com" path="/kappa/v2/sessions/:channel/reload" %}
  {% api-method-summary %}
    Refresh session aggregates
  {% endapi-method-summary %}

  {% api-method-description %}

  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="" type="string" required=false %}

        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}
