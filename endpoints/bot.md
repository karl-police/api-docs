# Bot

{% api-method method="get" host="https://api.streamelements.com" path="/kappa/v2/bot/:channel" %}
  {% api-method-summary %}
    Get bot status
  {% endapi-method-summary %}

  {% api-method-description %}
    Retrieve basic information about the bot status.
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="channel" type="string" required=true %}
          account/channel ID
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}

      {% api-method-headers %}
        {% api-method-parameter name="authorization" type="string" required=true %}
          authorization bearer token
        {% endapi-method-parameter %}
      {% endapi-method-headers %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```javascript
        {
        "bot": {
        "enabled": true,
        "name": "streamelements",
        "joined": true,
        "muted": false,
        "mod": true,
        "allowCustomName": true,
        "logs": [],
        "channel": "577c0455f9a31ea72a36b2b3"
        }
        }
        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="https://api.streamelements.com" path="/kappa/v2/bot/:channel/part" %}
  {% api-method-summary %}
    Join the bot
  {% endapi-method-summary %}

  {% api-method-description %}
    Make the bot join your channel.
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="channel" type="string" required=true %}
          account/channel ID
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}

      {% api-method-headers %}
        {% api-method-parameter name="authorization" type="string" required=true %}
          JWT Bearer token
        {% endapi-method-parameter %}
      {% endapi-method-headers %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```text

        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="https://api.streamelements.com" path="/kappa/v2/bot/:channel/join" %}
  {% api-method-summary %}
    Join the bot
  {% endapi-method-summary %}

  {% api-method-description %}
    Make the bot part your channel
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="channel" type="string" required=true %}
          Channel id
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}

      {% api-method-headers %}
        {% api-method-parameter name="authorization" type="string" required=true %}
          Channel id
        {% endapi-method-parameter %}
      {% endapi-method-headers %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```text

        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="https://api.streamelements.com" path="/kappa/v2/bot/:channel/mute" %}
  {% api-method-summary %}
    Mute the bot
  {% endapi-method-summary %}

  {% api-method-description %}
    Make the bot part your channel
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="channel" type="string" required=true %}
          Channel id
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}

      {% api-method-headers %}
        {% api-method-parameter name="authorization" type="string" required=true %}
          Channel id
        {% endapi-method-parameter %}
      {% endapi-method-headers %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```text

        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="https://api.streamelements.com" path="/kappa/v2/bot/:channel/unmute" %}
  {% api-method-summary %}
    Unmute the bot
  {% endapi-method-summary %}

  {% api-method-description %}
    Make the bot part your channel
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="channel" type="string" required=true %}
          Channel id
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}

      {% api-method-headers %}
        {% api-method-parameter name="authorization" type="string" required=true %}
          Channel id
        {% endapi-method-parameter %}
      {% endapi-method-headers %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```text

        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

## Modules

{% api-method method="get" host="https://api.streamelements.com" path="/kappa/v2/bot/modules/:channel" %}
  {% api-method-summary %}
    Get bot module settings
  {% endapi-method-summary %}

  {% api-method-description %}
    Retrieve the bot module settings
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="channel" type="string" required=true %}
          account/channel ID
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}

      {% api-method-headers %}
        {% api-method-parameter name="authorization" type="string" required=true %}
          authorization bearer token
        {% endapi-method-parameter %}
      {% endapi-method-headers %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

        ```
      {% endapi-method-response-example %}

      {% api-method-response-example httpCode=302 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```

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
