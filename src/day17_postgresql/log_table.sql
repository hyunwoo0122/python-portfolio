-- 로그 테이블 생성
CREATE TABLE logs (
    id SERIAL PRIMARY KEY,

    level VARCHAR(20) NOT NULL,

    created_at TIMESTAMPTZ DEFAULT NOW(),

    register_name VARCHAR(100),

    message TEXT NOT NULL,

    data JSONB
);

-- 자주 검색하는 컬럼에 인덱스 생성
CREATE INDEX idx_logs_level
ON logs(level);

CREATE INDEX idx_logs_created_at
ON logs(created_at);

CREATE INDEX idx_logs_register_name
ON logs(register_name);

-- JSONB 검색이 많다면 사용할 수 있는 GIN 인덱스
CREATE INDEX idx_logs_data
ON logs
USING GIN(data);