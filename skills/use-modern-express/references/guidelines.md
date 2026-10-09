# Express

## Versions and middleware

- Express 5 forwards rejected handler promises to error middleware; Express 4 needs its established explicit forwarding boundary.
- Order parsing/security/auth/routes/error handlers deliberately. Routers own cohesive resources; res.locals/explicit contexts own request state, not mutable module globals.
- Validate path/query/headers/body before domain work; set parser size limits. TS assertions are not validation.

## Responses and lifecycle

- Use four-argument error middleware after relevant routes; map domain failures to safe statuses/bodies and log unexpected causes without secrets/stacks in responses.
- Send once and return after send/next; if headers were sent, delegate errors through Express's established error path rather than sending again.
- Derive trust proxy, secure cookies/headers, CORS and allowed methods from ingress topology. Validate configuration at startup.
- Cookie-authenticated browser mutations require explicit CSRF protection; verify the application's token/origin checks and rejection behavior. CORS and HttpOnly cookies do not replace CSRF protection; GET must remain free of mutations.
- Long-lived servers stop new work on termination, close HTTP/database/queue resources and cancel timers/jobs with bounded shutdown. Serverless uses the host's lifecycle.

## Sources

- https://expressjs.com/en/guide/migrating-5.html
- https://expressjs.com/en/guide/error-handling.html
- https://expressjs.com/en/advanced/best-practice-security.html
- https://expressjs.com/en/guide/using-middleware.html
- [OWASP CSRF prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
