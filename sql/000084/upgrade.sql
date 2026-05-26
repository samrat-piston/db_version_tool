ALTER TABLE public."MavPaymentCode"
  ADD COLUMN IF NOT EXISTS vehicle_verified_by VARCHAR(50) NULL,
  ADD COLUMN IF NOT EXISTS is_map_version VARCHAR(50) NULL;

DO $$
BEGIN
    PERFORM 1
    FROM "ConfigData"
    WHERE "key" = 'verifone_preauth_amount';

    IF FOUND THEN
        UPDATE "ConfigData"
        SET "value" = '250'
        WHERE "key" = 'verifone_preauth_amount';
    ELSE
        INSERT INTO "ConfigData"
            ("name", "unit", "key", "value", "type")
        VALUES
            (
                'verifone_preauth_amount',
                'float',
                'verifone_preauth_amount',
                '250',
                '{admin}'
            );
    END IF;
END
$$;