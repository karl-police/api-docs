# Chatstats

{% api-method method="get" host="https://api.streamelements.com" path="/kappa/v2/chatstats/:username" %}
  {% api-method-summary %}
    Get channel
  {% endapi-method-summary %}

  {% api-method-description %}
    Get settings for a chatstats channel.
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="username" type="string" required=true %}
          The channels twitch username
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```javascript
        {
        "username": "stylerdev",
        "emotes": {
        "bttvChannelEmotes": {
        "KKaper": {
        "name": "KKaper",
        "_id": "566d3352fb7103f332d79dbe",
        "type": "bttv",
        "width": 28,
        "height": 28,
        "gif": true
        },
        "KKorner": {
        "name": "KKorner",
        "_id": "5674bb22bf317838643c7de9",
        "type": "bttv",
        "width": 28,
        "height": 28,
        "gif": true
        },
        "gachiGASM": {
        "name": "gachiGASM",
        "_id": "55999813f0db38ef6c7c663e",
        "type": "bttv",
        "width": 28,
        "height": 28,
        "gif": false
        },
        "pajaDank": {
        "name": "pajaDank",
        "_id": "568d840001ea6722348ab018",
        "type": "bttv",
        "width": 28,
        "height": 28,
        "gif": false
        },
        "pajaSWA": {
        "name": "pajaSWA",
        "_id": "5738dc6ad7a0b60d147270a0",
        "type": "bttv",
        "width": 28,
        "height": 28,
        "gif": true
        }
        },
        "bttvGlobalEmotes": {}
        },
        "lastMessage": "2018-05-09T15:13:38.792784692Z",
        "settings": {
        "ignoredChatters": {}
        }
        }
        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="https://api.streamelements.com" path="/kappa/v2/chatstats/?limit=5" %}
  {% api-method-summary %}
    Get top channels
  {% endapi-method-summary %}

  {% api-method-description %}
    Get top chatstats channels
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-query-parameters %}
        {% api-method-parameter name="limit" type="integer" required=false %}

        {% endapi-method-parameter %}

        {% api-method-parameter name="offset" type="integer" required=false %}

        {% endapi-method-parameter %}
      {% endapi-method-query-parameters %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```javascript
        [
        {
        "channel": "forsen",
        "messages": 93050644
        },
        {
        "channel": "sodapoppin",
        "messages": 50531988
        },
        {
        "channel": "twitchplayspokemon",
        "messages": 49843045
        },
        {
        "channel": "loltyler1",
        "messages": 43361492
        },
        {
        "channel": "reckful",
        "messages": 42596551
        }
        ]
        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="https://api.streamelements.com" path="/kappa/v2/chatstats/search" %}
  {% api-method-summary %}
    Search for channel
  {% endapi-method-summary %}

  {% api-method-description %}

  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-query-parameters %}
        {% api-method-parameter name="channel" type="string" required=true %}
          Channel username to search for
        {% endapi-method-parameter %}
      {% endapi-method-query-parameters %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```javascript
        [
        "xd00bsd",
        "xd1324bx",
        "xd13_",
        "xd191",
        "xd1as",
        "xd21395845",
        "xd24256121",
        "xd303",
        "xd3bit",
        "xd3ivid",
        "xd3mon3x",
        "xd3rn0",
        "xd3stroyah",
        "xd428777",
        "xd4475458",
        "xd4kfull",
        "xd4nkbuds420x",
        "xd4rk_galaxy",
        "xd4vv1d",
        "xd6912369xd",
        "xd7eem_",
        "xd9955613",
        "xd_alto",
        "xd_feeder",
        "xd_gaming_05",
        "xd_klykpl_xd",
        "xd_line",
        "xd_monky_xd",
        "xd_ozzie",
        "xd_regen",
        "xd_shadow323xd",
        "xd_sxc",
        "xdaawn",
        "xdabeat",
        "xdabxqueenx420x",
        "xdac0",
        "xdaddylonglegs",
        "xdadepsak",
        "xdaesae756",
        "xdaethstar",
        "xdaeyeonx",
        "xdafox",
        "xdaft_clueless",
        "xdagarwynn",
        "xdahveedx",
        "xdaisygaming",
        "xdakurlz",
        "xdalederiate",
        "xdaltx",
        "xdamineh"
        ]
        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="https://api.streamelements.com" path="/kappa/v2/chatstats/:username/stats" %}
  {% api-method-summary %}
    Get channel Stats
  {% endapi-method-summary %}

  {% api-method-description %}
    Returns the channels chatstats stats.
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="username" type="string" required=false %}
          The channels twitch username
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}

      {% api-method-query-parameters %}
        {% api-method-parameter name="limit" type="integer" required=false %}

        {% endapi-method-parameter %}
      {% endapi-method-query-parameters %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```javascript
        {
        "channel": "stylerdev",
        "totalMessages": 193581,
        "chatters": [
        { "name": "streamelements", "amount": 57177 }
        ],
        "hashtags": [
        { "hashtag": "#99", "amount": 256 },
        { "hashtag": "#9999", "amount": 136 }
        ],
        "commands": [
        { "command": "!commands", "amount": 596 },
        { "command": "!filters", "amount": 402 },
        { "command": "!ping", "amount": 381 },
        { "command": "!sr", "amount": 290 },
        { "command": "!cmd", "amount": 244 },
        { "command": "!points", "amount": 228 },
        { "command": "!uptime", "amount": 207 },
        { "command": "!l", "amount": 190 },
        { "command": "!xd", "amount": 187 },
        { "command": "!test", "amount": 161 },
        { "command": "!kappagen", "amount": 153 },
        { "command": "!voteskip", "amount": 138 },
        { "command": "!permit", "amount": 132 },
        { "command": "!command", "amount": 118 },
        { "command": "!redeem", "amount": 112 },
        { "command": "!clrtest", "amount": 90 },
        { "command": "!join", "amount": 87 },
        { "command": "!level", "amount": 84 },
        { "command": "!123", "amount": 81 },
        { "command": "!keepo", "amount": 80 },
        { "command": "!light", "amount": 74 },
        { "command": "!darko", "amount": 63 },
        { "command": "!bet", "amount": 61 },
        { "command": "!bot", "amount": 60 },
        { "command": "!color", "amount": 59 },
        { "command": "!kappa", "amount": 56 },
        { "command": "!bam", "amount": 55 },
        { "command": "!regulars", "amount": 51 }
        ],
        "bttvEmotes": [
        { "id": "566ca06065dbbdab32ec054e", "emote": "NaM", "amount": 2119 },
        { "id": "567b00c61ddbe1786688a633", "emote": "LuL", "amount": 1589 },
        { "id": "566ca00f65dbbdab32ec0544", "emote": "FishMoley", "amount": 344 },
        { "id": "54fbefeb01abde735115de5b", "emote": "TaxiBro", "amount": 332 },
        { "id": "55999813f0db38ef6c7c663e", "emote": "gachiGASM", "amount": 146 },
        { "id": "566ca38765dbbdab32ec0560", "emote": "SourPls", "amount": 135 },
        { "id": "566ca04265dbbdab32ec054a", "emote": "KKona", "amount": 102 },
        { "id": "550352766f86a5b26c281ba2", "emote": "VisLaud", "amount": 71 }
        ],
        "ffzEmotes": [],
        "twitchEmotes": [
        { "id": "1902", "emote": "Keepo", "amount": 14870 },
        { "id": "25", "emote": "Kappa", "amount": 13714 },
        { "id": "333116", "emote": "", "amount": 10512 },
        { "id": "689656", "emote": "gvdLOVE", "amount": 2454 },
        { "id": "898500", "emote": "gvdLOVE", "amount": 2263 },
        { "id": "171", "emote": "", "amount": 2137 },
        { "id": "598521", "emote": "", "amount": 2011 },
        { "id": "88", "emote": "PogChamp", "amount": 1452 },
        { "id": "190665", "emote": "", "amount": 1422 },
        { "id": "29049", "emote": "", "amount": 1109 },
        { "id": "120232", "emote": "TriHard", "amount": 493 },
        { "id": "445", "emote": "", "amount": 476 },
        { "id": "354", "emote": "4Head", "amount": 410 },
        { "id": "115848", "emote": "", "amount": 309 },
        { "id": "52", "emote": "SMOrc", "amount": 299 },
        { "id": "9", "emote": "", "amount": 280 },
        { "id": "3792", "emote": "ANELE", "amount": 142 },
        { "id": "68856", "emote": "MingLee", "amount": 137 },
        { "id": "80481", "emote": "pajaW", "amount": 135 },
        { "id": "41", "emote": "Kreygasm", "amount": 129 },
        { "id": "55338", "emote": "KappaPride", "amount": 126 },
        { "id": "1", "emote": "", "amount": 121 },
        { "id": "390795", "emote": "elementsS", "amount": 85 },
        { "id": "10327", "emote": "", "amount": 80 },
        { "id": "91", "emote": "", "amount": 68 },
        { "id": "9914", "emote": "", "amount": 67 },
        { "id": "9773", "emote": "", "amount": 67 },
        { "id": "9706", "emote": "", "amount": 67 },
        { "id": "96286", "emote": "", "amount": 67 },
        { "id": "95379", "emote": "", "amount": 67 },
        { "id": "9421", "emote": "", "amount": 67 },
        { "id": "89011", "emote": "", "amount": 67 },
        { "id": "87452", "emote": "", "amount": 67 },
        { "id": "86923", "emote": "", "amount": 67 },
        { "id": "85991", "emote": "", "amount": 67 },
        { "id": "85609", "emote": "", "amount": 67 },
        { "id": "83127", "emote": "", "amount": 67 },
        { "id": "81628", "emote": "", "amount": 67 },
        { "id": "73240", "emote": "", "amount": 67 },
        { "id": "72445", "emote": "", "amount": 67 },
        { "id": "65389", "emote": "", "amount": 67 },
        { "id": "58560", "emote": "", "amount": 67 },
        { "id": "57723", "emote": "", "amount": 67 },
        { "id": "57485", "emote": "", "amount": 67 },
        { "id": "57484", "emote": "", "amount": 67 },
        { "id": "55507", "emote": "", "amount": 67 },
        { "id": "50742", "emote": "", "amount": 67 },
        { "id": "50741", "emote": "", "amount": 67 },
        { "id": "50740", "emote": "", "amount": 67 },
        { "id": "50739", "emote": "", "amount": 67 },
        { "id": "48986", "emote": "", "amount": 67 },
        { "id": "48740", "emote": "", "amount": 67 },
        { "id": "48739", "emote": "", "amount": 67 },
        { "id": "45583", "emote": "", "amount": 67 },
        { "id": "4493", "emote": "", "amount": 67 },
        { "id": "40500", "emote": "", "amount": 67 },
        { "id": "37748", "emote": "", "amount": 67 },
        { "id": "29569", "emote": "", "amount": 67 },
        { "id": "2344", "emote": "", "amount": 67 },
        { "id": "23002", "emote": "", "amount": 67 },
        { "id": "2200", "emote": "lirikL", "amount": 67 },
        { "id": "2197", "emote": "", "amount": 67 },
        { "id": "2173", "emote": "", "amount": 67 },
        { "id": "2172", "emote": "lirikC", "amount": 67 },
        { "id": "1956", "emote": "lirikThump", "amount": 67 },
        { "id": "16156", "emote": "", "amount": 67 },
        { "id": "15020", "emote": "", "amount": 67 },
        { "id": "111486", "emote": "", "amount": 67 },
        { "id": "109208", "emote": "", "amount": 67 },
        { "id": "105098", "emote": "", "amount": 67 },
        { "id": "105054", "emote": "", "amount": 67 },
        { "id": "104403", "emote": "", "amount": 67 },
        { "id": "103436", "emote": "", "amount": 67 },
        { "id": "495772", "emote": "0x33Chair", "amount": 64 },
        { "id": "62835", "emote": "bleedPurple", "amount": 58 },
        { "id": "28", "emote": "MrDestructoid", "amount": 56 }
        ]
        }

        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="https://api.streamelements.com" path="/kappa/v2/chatstats/:username/epm" %}
  {% api-method-summary %}
    Get channel EPM
  {% endapi-method-summary %}

  {% api-method-description %}
    Returns a list of the emotes with the highest usage in the last minute.
  {% endapi-method-description %}

  {% api-method-spec %}
    {% api-method-request %}
      {% api-method-path-parameters %}
        {% api-method-parameter name="username" type="string" required=true %}
          The channels twitch username
        {% endapi-method-parameter %}
      {% endapi-method-path-parameters %}

      {% api-method-query-parameters %}
        {% api-method-parameter name="limit" type="integer" required=false %}

        {% endapi-method-parameter %}
      {% endapi-method-query-parameters %}
    {% endapi-method-request %}

    {% api-method-response %}
      {% api-method-response-example httpCode=200 %}
        {% api-method-response-example-description %}

        {% endapi-method-response-example-description %}

        ```javascript
        [
        {
        "id": "898500",
        "emote": "gvdLOVE",
        "provider": "twitch",
        "epm": 0
        },
        {
        "id": "88",
        "emote": "PogChamp",
        "provider": "twitch",
        "epm": 0
        },
        {
        "id": "390795",
        "emote": "elementsS",
        "provider": "twitch",
        "epm": 0
        }
        ]

        ```
      {% endapi-method-response-example %}
    {% endapi-method-response %}
  {% endapi-method-spec %}
{% endapi-method %}
