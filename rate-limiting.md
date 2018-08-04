# Rate Limiting

In order to guarantee API stability, there are a few rate limits in place. All endpoints that are rate limited have their `bucket` listed below. 

| Name | Request Count | Time Interval \(in seconds\) |
| --- | --- | --- | --- |
| global | 1000 | 60 |
| uploads | 50 | 60 |
| invitations | 10 | 60 |

If a limit is exceeded, an error is returned: HTTP 429 \(Too Many Requests\).

When you make an API request, you will receive a set of rate-limiting headers to help your application respond appropriately. The headers are:

`x-ratelimit-bucket` The bucket that you are currently using.

`x-ratelimit-remaining` The number of requests you have left for the current time interval.

`x-ratelimit-reset` A Unix epoch timestamp of when your rate-limit window will reset.
