# Provenance and timestamps

This directory holds independent, verifiable evidence of authorship and release
date for *Claude Code for Social Scientists*. None of it requires an account, a
fee, or a national copyright registration office.

## Files

- `timestamp.txt` records the author, the repository, the release, and the Git
  commit and tree hashes of the v3.0.1 release tree.
- `timestamp.txt.ots` is an [OpenTimestamps](https://opentimestamps.org) proof
  that anchors the SHA-256 digest of `timestamp.txt` to the Bitcoin blockchain.

## How the protection works

Copyright in this work is automatic. Under the Berne Convention it arises the
moment the work is fixed, in the author's jurisdictions (Türkiye, Greece,
Ireland) and in more than 180 member states, with no registration step. What a
rights holder needs in a dispute is not a registration but credible proof of
*what* was created and *when*. This repository establishes that proof in depth:

- **Zenodo (CERN)** mints a timestamped, citable DOI for each release, tied to
  the author's ORCID.
- **OpenTimestamps** anchors the release content to the Bitcoin blockchain, an
  independent and trustless time source.
- **The public Git history** is an append-only, content-addressed record of
  every change and its date.
- **The Creative Commons and Apache license declarations** state the terms in
  human- and machine-readable form.

Any one of these is persuasive. Together they are hard to dispute.

## Verifying the timestamp

With the OpenTimestamps client (`pip install opentimestamps-client`):

```bash
ots verify timestamp.txt.ots
```

The client confirms that the SHA-256 of `timestamp.txt` was submitted to the
OpenTimestamps calendars on the recorded date and, once the anchoring Bitcoin
block is mined, that it is attested on-chain. A freshly created proof is
calendar-attested immediately and upgrades to full Bitcoin attestation within
about a day:

```bash
ots upgrade timestamp.txt.ots
```

## Türkçe not

Bu dizin, eserin yazarlığını ve yayın tarihini bağımsız ve doğrulanabilir
biçimde kanıtlar. Hesap, ücret ya da tescil ofisi gerektirmez. Telif, Bern
Sözleşmesi gereği eser oluştuğu an Türkiye, Yunanistan, İrlanda ve 180'den fazla
ülkede kendiliğinden doğar. `timestamp.txt.ots`, dosyanın SHA-256 özetini
Bitcoin zincirine çapalayan bir OpenTimestamps kanıtıdır. Doğrulamak için
`ots verify timestamp.txt.ots` komutunu kullanınız.
