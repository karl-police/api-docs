# Activities

### Activity Types

| **Type** | **Provider** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| follow | Twitch |
| tip | Twitch & Youtube |
| host | Twitch |
| subscriber | Twitch & YouTube |
| cheer | Twitch |
| redemption | Twitch |
| sponsor | YouTube |
| superchat | YouTube |

### Activity Type

```javascript
{
    channel: Number;
    type: String;
    provider: String;
    providerId: String;
    createdAt: Date;
    flagged: Boolean;
    data: {
      username: String;
      tier: String;
      currency: String;
      amount: Number
      message: String;
      avatar: String;
      sender: String;
      gifted: Boolean;
    }
  }
```

{% api-method method="get" host="https://api.streamelements.com" path="/kappa/v2/activities/:channel" %}
  {% api-method-summary %}
    Get activities for a channel
  {% endapi-method-summary %}

  {% api-method-description %}
    This endpoint retrieves the activities for a channel.
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="channel" type="string" required=true %}
          account/channel ID
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}

      {% api-method-headers %}
        {% api-method-parameter name="authorization" required=true %}
          Authorization bearer token
        {% endapi-method-parameter %}
      {% endapi-method-headers %}

      {% api-method-query-parameters %}
        {% api-method-parameter type="string" name="after" required=false %}
          An ISO8601 date string.
        {% endapi-method-parameter %}

        {% api-method-parameter type="string" name="before" %}
          An ISO8601 date string
        {% endapi-method-parameter %}

        {% api-method-parameter name="username" type="string" required=false %}
          Search activities for a specific username
        {% endapi-method-parameter %}

        {% api-method-parameter name="limit" type="number" required=false %}
          Limit the number of activities to return \(default 100 when no limit is specified\)
        {% endapi-method-parameter %}

        {% api-method-parameter name="offset" type="number" required=false %}
          Pagination offset
        {% endapi-method-parameter %}

        {% api-method-parameter name="types" type="string" required=true %}
          Types can be added to only return specific types of activities
        {% endapi-method-parameter %}
      {% endapi-method-query-parameters %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}
          Activities successfully retrieved.
        {% endapi-method-response-example-description %}

        ```javascript
        [
        {
        "_id": "59e25ed28f25ce00010a0212",
        "channel": "59e10187207b2900014d14d9",
        "type": "tip",
        "data": {
        "tipId": "59e25ed28f25ce00010a0211",
        "username": "xd",
        "amount": 21,
        "currency": "USD",
        "message": "NaM"
        },
        "createdAt": "2017-10-14T19:00:34.324Z",
        "provider": "twitch"
        }
        ]
        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=302 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=401 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=403 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=404 %}
        {% api-method-response-example-description %}
          Could not find a cake matching this query.
        {% endapi-method-response-example-description %}

        ```javascript
        {
        "statusCode": 404,
        "error": "Not Found"
        }
        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="https://api.streamelements.com" path="/kappa/v2/activities/:channel/:activityId" %}
  {% api-method-summary %}
    Get a single activity for a channel
  {% endapi-method-summary %}

  {% api-method-description %}
    This endpoint retrieves a single activity for a channel.
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="channel" type="string" required=true %}
          account/channel ID
        {% endapi-method-parameter %}

        {% api-method-parameter name="activityId" type="string" required=true %}
          activity ID
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}

      {% api-method-headers %}
        {% api-method-parameter name="authorization" required=true %}
          Authorization bearer token
        {% endapi-method-parameter %}
      {% endapi-method-headers %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```javascript
        {
        "_id": "59e25ed28f25ce00010a0212",
        "channel": "59e10187207b2900014d14d9",
        "type": "tip",
        "data": {
        "tipId": "59e25ed28f25ce00010a0211",
        "username": "xd",
        "amount": 21,
        "currency": "USD",
        "message": "NaM"
        },
        "createdAt": "2017-10-14T19:00:34.324Z",
        "provider": "twitch"
        }
        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=400 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```javascript
        {
        "statusCode": 400,
        "error": "Bad Request",
        "message": "child \"channel\" fails because [\"channel\" with value \"57209398234\" fails to match the required pattern: /^[0-9a-fA-F]{24}$/]",
        "details": [
          {
              "path": [
              "channel"
              ],
              "message": "\"channel\" with value \"57209398234\" fails to match the required pattern: /^[0-9a-fA-F]{24}$/"
          }
        ]
        }
        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=401 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```javascript
        {
        "statusCode": 401,
        "error": "Unauthorized",
        "message": "No authorization token was found"
        }
        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=403 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=404 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```javascript
        {
        "statusCode": 404,
        "error": "Not Found"
        }
        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="https://api.streamelements.com" path="/kappa/v2/activities/:channel/:activityId/replay" %}
  {% api-method-summary %}
    Replay an activity
  {% endapi-method-summary %}

  {% api-method-description %}
    This endpoint will replay the alert for an activity.
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="channel" type="string" required=true %}
          account/channel ID
        {% endapi-method-parameter %}

        {% api-method-parameter name="activityId" type="string" required=true %}
          activity ID
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}

      {% api-method-headers %}
        {% api-method-parameter name="authorization" type="string" required=true %}
          Authorization bearer token
        {% endapi-method-parameter %}
      {% endapi-method-headers %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```
        {"success":true}
        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=304 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=400 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=401 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=403 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=404 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=500 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=503 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}
