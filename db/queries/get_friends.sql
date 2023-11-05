-- :name get_friends :many
select user2_id from friendship where user1_id = :user_id