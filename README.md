# ai_customer_support_agent
Solar Panels Customer support Strands Agent with Responsible AI uing guardrails.

mkdir -p ./{src/app/{agents,tools,services,models,utils},data/{raw,embeddings},scripts,tests}


ai-agent-project/
│
├── pyproject.toml
├── uv.lock
├── README.md
├── .env
│
├── src/
│   └── app/
│       │
│       ├── main.py            # entry point
│       ├── config.py          # env config
│       │
│       ├── agents/            # AI agents
│       │   ├── planner_agent.py
│       │   ├── research_agent.py
│       │   └── qa_agent.py
│       │
│       ├── tools/             # tools agents use
│       │   ├── web_search.py
│       │   ├── calculator.py
│       │   └── vector_search.py
│       │
│       ├── services/          # business logic
│       │   ├── rag_service.py
│       │   └── document_service.py
│       │
│       ├── models/            # data models
│       │   └── document.py
│       │
│       └── utils/             # helpers
│           └── logger.py
│
├── data/
│   ├── raw/
│   └── embeddings/
│
├── scripts/
│   └── ingest_documents.py
│
└── tests/
    └── test_agents.py