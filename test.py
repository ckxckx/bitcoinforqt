from json import *
oo='''
{
"vout_sz": 2,
"received": "2017-05-10T13:20:25.519916323Z",
"lock_time": 0,
"hash": "dc20cdfd1e409cce6de8def9eb3b6c0ad7411dfc055204cb1e521eed3d8869e3",
"addresses": [
"mgN94Z7hRWy4UfZHTj2T8hZd1BctusLkps",
"mzPnKxCTMF3Dx9Nx9ktZ6n72LFheEX3MpQ"
],
"inputs": [
{
"addresses": [
"mgN94Z7hRWy4UfZHTj2T8hZd1BctusLkps"
],
"script": "483045022100f02bd30f926528b7ffcac0da4283c7494ef79bf5a4ae9d1c91a11e2c22fb3347022056abbd4997025093a56f3403170c838f790ad9c408822395ca0a6deea1733ed1012103565b4d5d01b7ecca773a57df552ce0a2ea63ab0bbfa69fd5958de99c5e62e36e",
"sequence": 4294967295,
"output_value": 155798,
"output_index": 1,
"prev_hash": "ef4351885fa3910d6654f1b4bda06033519f603460b7fa225c0659af994f4ec8",
"script_type": "pay-to-pubkey-hash"
}
],
"outputs": [
{
"script_type": "pay-to-pubkey-hash",
"addresses": [
"mzPnKxCTMF3Dx9Nx9ktZ6n72LFheEX3MpQ"
],
"value": 1,
"script": "76a914cf0f286c587aeef3dd0293c00dabb90c47da0a8388ac"
},
{
"script_type": "pay-to-pubkey-hash",
"addresses": [
"mgN94Z7hRWy4UfZHTj2T8hZd1BctusLkps"
],
"value": 112697,
"script": "76a914094d5ec3d22b64175fcf316d6fd2940e2c4ae84688ac"
}
],
"relayed_by": "60.207.237.115",
"block_height": -1,
"block_index": -1,
"vin_sz": 1,
"preference": "high",
"confirmations": 0,
"fees": 43100,
"version": 1,
"double_spend": false,
"total": 112698,
"size": 226
}
'''
oo=loads(oo)
type(oo)


bb='''
{
  "hash": "cca7507897abc89628f450e8b1e0c6fca4ec3f7b34cccf55f3f531c659ff4d79",
  "ver": 1,
  "vin_sz": 1,
  "vout_sz": 2,
  "lock_time": 0,
  "size": 300,
  "in": [
    {
      "prev_out": {
        "hash": "a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d",
        "n": 0
      },
      "scriptSig": "30450221009908144ca6539e09512b9295c8a27050d478fbb96f8addbc3d075544dc41328702201aa528be2b907d316d2da068dd9eb1e23243d97e444d59290d2fddf25269ee0e01 042e930f39ba62c6534ee98ed20ca98959d34aa9e057cda01cfd422c6bab3667b76426529382c23f42b9b08d7832d4fee1d6b437a8526e59667ce9c4e9dcebcabb"
    }
  ],
  "out": [
    {
      "value": "5777.00000000",
      "scriptPubKey": "OP_DUP OP_HASH160 df1bd49a6c9e34dfa8631f2c54cf39986027501b OP_EQUALVERIFY OP_CHECKSIG",
      "address": "1MLh2UVHgonJY4ZtsakoXtkcXDJ2EPU6RY",
      "next_in": {
        "hash": "3b8328fe7e53a8162cf023738a53c85a3cbf21efe517ab878e8cfecc3a2e22db",
        "n": 0
      }
    },
    {
      "value": "4223.00000000",
      "scriptPubKey": "04cd5e9726e6afeae357b1806be25a4c3d3811775835d235417ea746b7db9eeab33cf01674b944c64561ce3388fa1abd0fa88b06c44ce81e2234aa70fe578d455d OP_CHECKSIG",
      "next_in": {
        "hash": "9e744590d196b63d02a1dd7ef596fd6082286f84295d66da411a9ffebfdd1957",
        "n": 10
      }
    }
  ],
  "nid": "1aed0e7cd223f973090d55da33a574312707d2cc4a4f4a5c70d6bbdc88b14cd1",
  "block": "0000000013ab9f8ed78b254a429d3d5ad52905362e01bf6c682940337721eb51",
  "blocknumber": 57044,
  "time": "2010-05-22 18:26:08"
}
'''


qqq='''
01000000016587ed26682ba0991643c572a74d57525aa259aefae3d68475e12ef9befc98b6010000006b483045022100f64d100c1d33666dfb149fab0b066ed9047c04645821154c176f49f6ae818bfa02200a6f59346da02de6de0ba510672eb4606ba36a2a39fffe60f4e4c7e26983564301210316cff587a01a2736d5e12e53551b18d73780b83c3bfb4fcf209c869b11b6415effffffff02801a0600000000001976a914094d5ec3d22b64175fcf316d6fd2940e2c4ae84688ace5236541000000001976a914c01a7ca16b47be50cbdbc60724f701d52d75156688ac00000000
'''