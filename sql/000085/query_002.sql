Update "GasStation" SET is_gas_cp = true WHERE is_gas_cp IS NULL;
SELECT * FROM "GasStation" WHERE is_gas_cp IS NULL;
