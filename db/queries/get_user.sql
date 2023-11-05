-- :name get_user :one
select user_id from user where firebase_uid = :firebase_uid