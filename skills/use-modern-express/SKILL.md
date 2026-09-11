---
name: use-modern-express
description: "Use version-aware Express routing, middleware, error handling, security, and graceful-shutdown idioms when writing, modifying, fixing, or reviewing Node.js applications."
---

# Modern Express

Use for Express applications and APIs. Pair with `use-modern-javascript` or
`use-modern-typescript` for language and Node.js rules.

## Target resolution

Read `package.json` for the Express version, Node.js `engines`, module type, and
the JavaScript or TypeScript build target. Establish whether the app runs behind
a trusted proxy, in a serverless host, or as a long-lived Node.js process before
using lifecycle or request-network behavior.


## Working rules

- Keep middleware order explicit. Put request parsing, security policy,
  authentication, routing, and error handling in an order that matches the trust
  boundary.
- Use Express 5 promise handling when the target supports it; still centralize
  error translation in error middleware and preserve original causes for logs.
- Validate and normalize request data at the route boundary. Set deliberate body
  size limits and return consistent status and error shapes.
- Send one response per request. After a response or `next(err)`, return from the
  current handler and do not continue mutating the response.
- Configure `trust proxy`, cookies, headers, CORS, and allowed methods for the
  deployment topology; never inherit a permissive production default by
  accident.
- Keep process shutdown explicit: stop accepting work, close the server, cancel
  owned background work, and exit with a meaningful status.

Read `references/guidelines.md` for Express 5, middleware, errors, security, and
process-lifecycle rules.
