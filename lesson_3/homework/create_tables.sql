CREATE TABLE IF NOT EXISTS terminal (
  id            INTEGER PRIMARY KEY,
  configuration TEXT               ,
  title         TEXT,
  comment       TEXT,
  pub_key       TEXT
);

CREATE TABLE IF NOT EXISTS partner (
  id      INTEGER PRIMARY KEY,
  title   TEXT               ,
  comment TEXT
);

CREATE TABLE IF NOT EXISTS credit (
  id         INTEGER PRIMARY KEY,
  partner_id INTEGER            ,
  datetime   DATETIME           ,
  summ       INTEGER            ,
  FOREIGN KEY (partner_id) REFERENCES partner (id)
);

CREATE TABLE IF NOT EXISTS debit (
  id         INTEGER PRIMARY KEY,
  partner_id INTEGER            ,
  datetime   DATETIME           ,
  summ       INTEGER            ,
  FOREIGN KEY (partner_id) REFERENCES partner (id)
);

CREATE TABLE IF NOT EXISTS payment (
  id             INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
  datetime       DATETIME           ,
  terminal_id    INTEGER            ,
  transaction_id INTEGER            ,
  partner_id     INTEGER            ,
  summ           INTEGER            ,
  FOREIGN KEY (terminal_id) REFERENCES terminal (id),
  FOREIGN KEY (partner_id) REFERENCES partner (id)
);
