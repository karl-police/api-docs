# Points

{% api-method method="put" host="https://api.streamelements.com" path="/kappa/v2/points/:channel" %}
  {% api-method-summary %}
    Bulk update points
  {% endapi-method-summary %}

  {% api-method-description %}
    Bulk update many users points across multiple leaderboards.
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="channel" type="string" required=true %}
          The channel Id
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}

      {% api-method-body-parameters %}
        {% api-method-parameter name="users" type="array" required=true %}
          Allow fields:  
          `username`The username of the user.  
          `current` The amount of points.  
          `alltime` The alltime amount of points. \(optional\)  
          `twitchId` The users twitchId. \(optional\)  
          `timeOnline` Time in minutes. \(optional\)  
          `timeOffline` Time in minutes. \(optional\)
        {% endapi-method-parameter %}

        {% api-method-parameter name="mode" type="string" required=true %}

          **`set`** Will overwrite the users points if found.  
          **`add`** Will add points to an existing. 
        {% endapi-method-parameter %}
      {% endapi-method-body-parameters %}
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

{% api-method method="put" host="https://api.streamelements.com" path="/kappa/v2/points/:channel/:user/:amount" %}
  {% api-method-summary %}
    Update a users points
  {% endapi-method-summary %}

  {% api-method-description %}
    Adds or removes points from a user in the current leaderboard.  

    channel
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="channel" type="string" required=true %}
          The channel Id.
        {% endapi-method-parameter %}

        {% api-method-parameter name="user" type="string" required=true %}
          The target user.
        {% endapi-method-parameter %}

        {% api-method-parameter name="amount" type="integer" required=true %}
          The amount of points.
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

{% api-method method="put" host="https://api.streamelements.com" path="/kappa/v2/points/:channel/alltime/:user/:amount" %}
  {% api-method-summary %}
    Update a users alltime points
  {% endapi-method-summary %}

  {% api-method-description %}

  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="channel" type="string" required=false %}

        {% endapi-method-parameter %}

        {% api-method-parameter name="user" type="string" required=false %}

        {% endapi-method-parameter %}

        {% api-method-parameter name="amount" type="integer" required=false %}
          The amount of points.
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

{% api-method method="delete" host="" path="" %}
  {% api-method-summary %}
    Reset the current leaderboard
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

{% api-method method="delete" host="" path="" %}
  {% api-method-summary %}
    Reset the alltime leaderboard
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

{% api-method method="get" host="" path="" %}
  {% api-method-summary %}

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
