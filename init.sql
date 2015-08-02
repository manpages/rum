CREATE TABLE IF NOT EXISTS agreements (
  id            INTEGER      NOT NULL        PRIMARY KEY   AUTOINCREMENT
 ,number        VARCHAR(255) NOT NULL UNIQUE
 ,password      VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS devices (
  id            INTEGER      NOT NULL        PRIMARY KEY   AUTOINCREMENT
 ,name          VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS sessions (
  agreement     INTEGER      NOT NULL        REFERENCES   agreements(id)
 ,device        INTEGER      NOT NULL        REFERENCES      devices(id)
 ,token         VARCHAR(255) NOT NULL
 ,PRIMARY KEY (agreement, device)
);

CREATE TABLE IF NOT EXISTS calls (
  id            INTEGER      NOT NULL        PRIMARY KEY   AUTOINCREMENT
 ,agreement     INTEGER      NOT NULL        REFERENCES   agreements(id)
 ,device        INTEGER      NOT NULL        REFERENCES      devices(id)
 ,active        BOOLEAN      NOT NULL                                      DEFAULT True
 ,latitude      VARCHAR(255) NOT NULL
 ,longitude     VARCHAR(255) NOT NULL
 ,message       VARCHAR(255)                                               DEFAULT NULL
 ,received      INTEGER      NOT NULL
 ,beamed        INTEGER      NOT NULL
);
