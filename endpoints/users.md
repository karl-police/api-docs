# Users

{% api-method method="get" host="https://api.streamelements.com" path="kappa/v2/uploads/:channel_id" %}
{% api-method-summary %}
Get uploads (Auth Token required)
{% endapi-method-summary %}

{% api-method-description %} Gets uploads from a channel. (Auth Token required) {% endapi-method-description %}

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

```javascript
{
uploads":[{
  "deleted":false,
  "_id":"5da714032877f32fba8fa4f6",
  "channel":"channel id to which the upload belongs to","uuid":"unique id for the image",
  "name":"Original file name","size":Image size in Bytes but it is bigger for some reason,
  "url":"https://cdn.streamelements.com/uploads/UUID.filetype",
  "type":"image/png upload type in array",
  "createdAt":"time default format",
  "updatedAt":"time default format"}
  ]}
}
```
