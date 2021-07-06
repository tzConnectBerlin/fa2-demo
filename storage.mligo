 {
  admin = {
    admin = ("tz1RjonN5qEJM8cZhKcfGyoEqhw1FNB4ti6w" : address);
    pending_admin = (None : address option);
    paused = true;
  };
  assets = {
    ledger = (Big_map.empty : ledger);
    operators = (Big_map.empty : operator_storage);
    token_total_supply = (Big_map.empty : token_total_supply);
    token_metadata = (Big_map.empty : token_metadata_storage);
    permissions = {
      operator = Owner_or_operator_transfer;
      receiver = Optional_owner_hook;
      sender = Owner_no_hook;
      custom = (None : custom_permission_policy option);
    };
  };
  metadata = Big_map.literal [
    ("", Bytes.pack "tezos-storage:content" );
    (* ("", 0x74657a6f732d73746f726167653a636f6e74656e74); *)
    ("content", 0x00) (* bytes encoded UTF-8 JSON *)
  ];
}
