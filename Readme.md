api_work/
├── GET/
│   ├── path_parameters.py
│   ├── query_parameters.py
│   ├── optional_parameter.py
│   └── parameter_validation.py
│
├── POST/
│   ├── request_body.py
│   ├── nested_models.py
│   ├── field_validation.py
│   ├── multiple_bodies.py
│   ├── body_with_path.py
│   └── body_with_query.py
│
├── PUT/
│   ├── full_update.py
│   ├── partial_update.py
│   └── put_with_path.py
│
├── DELETE/
│   ├── delete_basic.py
│   ├── delete_with_response.py
│   ├── delete_with_query.py
│   ├── delete_validation.py
│   └── delete_multiple.py
│
├── ROUTING/
│   ├── include_router.py
│   ├── route_prefix.py
│   └── route_tags.py
│
├── RESPONSE/
│   ├── response_model.py
│   ├── status_codes.py
│   ├── custom_response.py
│   └── error_handling.py
│
├── MIDDLEWARE/
│   ├── basic_middleware.py
│   ├── cors_middleware.py
│   └── logging_middleware.py
│
├── DEPENDENCIES/
│   ├── basic_dependency.py
│   ├── dependency_chain.py
│   └── db_dependency.py
│
├── AUTH/
│   ├── api_key_auth.py
│   ├── http_basic_auth.py
│   └── jwt_auth.py
│
├── BACKGROUND/
│   ├── basic_task.py
│   └── task_with_deps.py
│
├── FILES/
│   ├── file_upload.py
│   ├── multiple_files.py
│   └── file_download.py
│
├── DATABASE/
│   ├── sqlalchemy_setup.py
│   ├── crud_operations.py
│   └── alembic_migration.py
│
├── TESTING/
│   ├── test_get.py
│   ├── test_post.py
│   ├── test_auth.py
│   └── conftest.py
│
├── MINI_PROJECT/
│   └── task_manager/
│       ├── main.py
│       ├── models/
│       │   └── task.py
│       ├── schemas/
│       │   └── task.py
│       ├── routers/
│       │   └── tasks.py
│       ├── services/
│       │   └── email_service.py
│       ├── db/
│       │   └── session.py
│       └── tests/
│           └── test_tasks.py
│
└── requirements.txt