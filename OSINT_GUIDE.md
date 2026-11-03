# Practical OSINT Safety Guide

Open-source intelligence is the disciplined collection and analysis of information that is lawfully and appropriately available to the researcher. A public repository, public webpage, or open-source license does not automatically make a tool safe, accurate, lawful for every use, or appropriate for collecting personal data.

## 1. Define a legitimate research question

- State the public-interest, defensive, academic, or authorized purpose.
- Limit collection to information necessary for that purpose.
- Avoid targeting private individuals, exposing sensitive personal information, or enabling harassment, stalking, doxxing, or unauthorized access.
- Do not bypass authentication, access controls, paywalls, or technical restrictions.

## 2. Evaluate a tool before running it

Review the upstream source and release history. Check:

- Maintainer identity and project activity, without treating popularity as proof of trust.
- License and third-party data terms.
- Install scripts, dependencies, binary downloads, and requested privileges.
- Network destinations, telemetry, credential handling, and filesystem access.
- Security policy, open advisories, and known limitations.

Prefer source builds or verifiable releases when practical. A source-available tool can still contain malicious or vulnerable code.

## 3. Isolate experiments

- Use a disposable VM or container appropriate to the tool's risk.
- Do not mount personal folders, SSH keys, browser profiles, cloud credentials, or production secrets.
- Use least privilege and restrict network access where practical.
- Take snapshots and discard the environment after testing.
- Never run an unknown script with administrator/root privileges merely to make it work.

## 4. Preserve evidence responsibly

For each observation, record the source URL, collection timestamp, tool/version, query or collection method, and any transformations. Keep original observations separate from analyst interpretation. Record uncertainty and conflicting evidence. A hash can detect later file changes, but does not prove that a source is authentic or that a claim is true.

Minimize retention of personal data. Apply access controls and deletion schedules appropriate to the research purpose and applicable law.

## 5. Respect platform and legal boundaries

Follow applicable law, platform terms, copyright and database rights, rate limits, and privacy requirements. Do not use OSINT tools to threaten, intimidate, discriminate against, or facilitate harm to people. When a collection method is unclear or unauthorized, stop and obtain appropriate guidance.

## 6. Report findings carefully

Separate:
- **Observed:** directly recorded source material.
- **Corroborated:** supported by independent sources.
- **Inferred:** an interpretation based on available evidence.
- **Unknown:** not established by the evidence.

Avoid presenting automated matches, identity guesses, or risk scores as facts. Provide context, confidence, limitations, and a correction path.

## Project AVI status

This guide is general orientation only. Project AVI does not currently implement collection, evidence storage, sandboxing, automated analysis, or reporting tools.
