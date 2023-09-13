import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app="dev:app",
        app_dir="api",
        host="0.0.0.0",
        reload=True,
        reload_includes=[
            "api/**/*.py",
            "public/**/*.css",
            "public/**/*.html",
            "public/**/*.jinja2",
        ],
    )
