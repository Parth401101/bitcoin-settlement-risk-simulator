# Bitcoin Settlement Risk Simulator

A Python-based simulation framework modeling Bitcoin probabilistic finality, reorg risk, and solver capital exposure in cross-chain bridge systems.

## Overview

Bitcoin provides probabilistic finality — transactions become increasingly secure as confirmations accumulate, but are never instantly final. 

This project models the economic and adversarial risks faced by liquidity solvers who advance capital against unfinalized Bitcoin transactions in bridge-like architectures.

Rather than focusing on UI or token minting mechanics, this simulator studies:

- Mempool dynamics
- Fee-based block selection
- Confirmation depth modeling
- Chain reorganization probability
- Double-spend scenarios
- Solver confirmation policies
- Capital exposure and insolvency risk

The goal is to explore how confirmation latency, attacker hashpower, and solver strategy interact in adversarial environments.

## Why This Matters

Solver-based bridge systems require advancing liquidity before Bitcoin achieves strong settlement assurance. Acting too early introduces reorg and double-spend risk. Acting too late reduces competitiveness.

This simulator provides a controlled environment to study:

- Optimal confirmation thresholds
- Risk-adjusted solver behavior
- Economic survivability under adversarial conditions
- Trade-offs between speed and security

## Scope

This is a research-oriented simulation. It does not connect to mainnet or testnet. Instead, it models Bitcoin network behavior abstractly to analyze settlement risk dynamics.

Future extensions include:
- Competitive solver markets
- Intent-based routing layer
- Dynamic pricing models
- Capital constraints and bankruptcy simulation
