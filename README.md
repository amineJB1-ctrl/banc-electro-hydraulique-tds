# Electro-hydraulic Test Bench — Technical Documentation

Complete teaching material for an industrial electro-hydraulic bench (TDS DIDACTIC),
produced during a 4-month end-of-studies internship at **Technology Development Systems
(TDS-Sfax)**, an ISO 9001 certified company.

**Live documentation site → [banc-hydraulique-tds.netlify.app](https://banc-hydraulique-tds.netlify.app/)** *(in French)*

---

## What this is

A 14-chapter course and 6 practical lab exercises covering the full architecture of an
electro-hydraulic training bench: energy chain, hydraulic actuators, solenoid valves,
sensors and instrumentation, PLC control, regulation and safety devices — with schematics
drawn to the **ISO 1219** and **IEC 60617** standards.

## My contribution

I designed and wrote the entire teaching material: the 14 chapters, the 6 lab exercises,
the Ladder programs and the HMI screens. The bench wiring was carried out jointly with my
internship partner, who wrote the internship report (not included in this repository).

## Contents

| Folder | What's inside |
|---|---|
| `docs/` | Sphinx sources of the documentation site (reStructuredText) |
| `automatisme/ladder/` | DELTA DVP Ladder programs (ISPSoft) — screenshots |
| `automatisme/ihm/` | 7-inch HMI supervision screens (DOPSoft) — screenshots |
| `automatisme/grafcet/` | GRAFCET models of the sequential control |
| `schemas/` | Hydraulic and electrical schematics (ISO 1219 / IEC 60617) |
| `fluidsim/` | FluidSIM circuit simulations |
| `tp/` | The 6 lab exercises |

## Tools

Sphinx · reStructuredText · Netlify · ISPSoft (DELTA DVP) · DOPSoft · FluidSIM

## Rights

Bench and equipment: **TDS DIDACTIC**. Published with the agreement of TDS-Sfax.
This material may be consulted for reference. It is **not** released under an open-source
licence: any reuse, reproduction or redistribution requires the agreement of TDS-Sfax.

© 2026 Mohamed Amine Jabeur — teaching material
