alter table "MavPaymentCode" drop column if exists vehicle_verified_by;
alter table "MavPaymentCode" drop column if exists is_map_version;
delete from "ConfigData" where "key" = 'verifone_preauth_amount';