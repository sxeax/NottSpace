CREATE TABLE IF NOT EXISTS "user" (
    "user_id" integer,
    "firebase_uid" text NOT NULL,
    "display_name" text NOT NULL,
    "bio" text,
    "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY ("user_id")
);

CREATE TABLE IF NOT EXISTS "post" (
    "post_id" integer,
    "user_id" integer,
    "content" numeric,
    "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY ("post_id")
);

CREATE TABLE IF NOT EXISTS "friendship" (
    "friendship_id" integer,
    "user1_id" integer NOT NULL,
    "user2_id" integer NOT NULL,
    FOREIGN KEY ("user1_id") REFERENCES "user" ("user_id"),
    FOREIGN KEY ("user2_id") REFERENCES "user" ("user_id"),
    PRIMARY KEY ("friendship_id")
);

CREATE TABLE IF NOT EXISTS "group" (
    "group_id" integer,
    "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY ("group_id")
);

CREATE TABLE IF NOT EXISTS "message" (
    "message_id" integer,
    "sender_id" integer NOT NULL,
    "group_id" integer NOT NULL,
    "content" text NOT NULL,
    "sent_at" DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY ("group_id") REFERENCES "group" ("group_id"),
    FOREIGN KEY ("sender_id") REFERENCES "group" ("user_id"),
    PRIMARY KEY ("message_id")
);

