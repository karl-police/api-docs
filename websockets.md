# Websockets

## Socket.io

Socket.io is a real-time publish/subscribe notification system.



#### Basic example of how to connect

```javascript
import io from 'socket.io-client';

// Your StreamElements JWT
const accessToken = '';

const socket = io('https://realtime.streamelements.com', {
    transports: ['websocket']
});

// Socket connected
socket.on('connect', onConnect);

// Socket got disconnected
socket.on('disconnect', onDisconnect);

// Socket is authenticated
socket.on('authenticated', onAuthenticated);

// New event received
socket.on('event', onEvent);

function onConnect() {
    console.log('Successfully connected to the websocket'):

    socket.emit('authenticate', { method: 'jwt', token: accessToken }));
}

function onDisconnect() {
    console.log('Disconnected from websocket')
    // Reconnect
}

function onAuthenticated(data) {
    const { channelId } = data;

    console.log(`Successfully connected to channel ${channelId}`);
}

function onEvent(event) {
    // Deal with events
}
```

### Events

| Event | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| connect | Sent when the websocket is connected |
| disconnect | Sent once the websocket disconnects |
| authenticated | Sent once the websocket is fully authenticated |
| event:update | Sent when a session value is updated |
| event | Sent when a new activity is registered |
| overlay:refresh | Sent when an overlay reload command is issued |
| session:reset | Sent when a session is reset |

{% tabs %}
  {% tab title="Songrequest" %}

  {% endtab %}

  {% tab title="Second Tab" %}

  {% endtab %}
{% endtabs %}
