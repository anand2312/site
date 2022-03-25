use serde_json::{json, Value};
use worker::*;

mod utils;


fn log_request(req: &Request) {
    console_log!(
        "{} - [{}], located at: {:?}, within: {}",
        Date::now().to_string(),
        req.path(),
        req.cf().coordinates().unwrap_or_default(),
        req.cf().region().unwrap_or("unknown region".into())
    );
}

async fn get_pinned_repos<T>(_: Request, ctx: RouteContext<T>) -> Result<Response> {
    let kv = ctx.kv("REPOS")?;
    let data = kv.get("cached").text().await?.unwrap();
    let json: Value = serde_json::from_str(data.as_str())?;
    let to_return = json!({"data": json});
    return Response::from_json(&to_return);
}

#[event(fetch)]
pub async fn main(req: Request, env: Env, _ctx: worker::Context) -> Result<Response> {
    log_request(&req);
    utils::set_panic_hook();

    let router = Router::new();

    router
        .get("/", |_, _| Response::ok("Hello!"))
        .get_async("/pinned", get_pinned_repos)
        .get("/worker-version", |_, ctx| {
            let version = ctx.var("WORKERS_RS_VERSION")?.to_string();
            Response::ok(version)
        })
        .run(req, env)
        .await
}
