-- :name get_user :one
select * from user where firebase_uid = :firebase_uid
