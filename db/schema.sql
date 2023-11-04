CREATE TABLE IF NOT EXISTS "user" (
	"user_id"	INTEGER,
	"firebase_uid" TEXT NOT NULL,
	"bio"	TEXT,
	PRIMARY KEY("user_id")
);
CREATE TABLE IF NOT EXISTS "post" (
	"post_id"	INTEGER,
	"user_id"	INTEGER,
	"content"	NUMERIC,
	"timestamp"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("post_id")
);
CREATE TABLE IF NOT EXISTS "friendship" (
	"friendship_id"	INTEGER,
	"user1_id"	INTEGER NOT NULL,
	"user2_id"	INTEGER NOT NULL,
	FOREIGN KEY("user1_id") REFERENCES "user" ("user_id"),
	FOREIGN KEY("user2_id") REFERENCES "user"("user_id"),
	PRIMARY KEY("friendship_id")
);
CREATE TABLE IF NOT EXISTS "group" (
	"group_id"	INTEGER,
	"creation_date"	DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
	PRIMARY KEY("group_id")
);
CREATE TABLE IF NOT EXISTS "message" (
	"message_id"	INTEGER,
	"sender_id"	INTEGER NOT NULL,
	"group_id"	INTEGER NOT NULL,
	"content"	TEXT NOT NULL,
	"sent_at"	DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "group" ("group_id"),
	FOREIGN KEY("sender_id") REFERENCES "group" ("user_id"),
	PRIMARY KEY("message_id")
);
