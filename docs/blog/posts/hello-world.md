---
draft: true 
date: 2025-01-15
categories:
  - Crypto
  - Coinbase
  - Smart Contracts
---

# Smart Contracts 101: A Beginner's Guide using Coinbase SDK

## Introduction

The purpose of this post is to help those new to developing Blockchain technology understand Smart Contracts and how they work. Continue reading to understand their use cases in depth.

### Prerequisites

It is assumed that you have already completed the [Getting Started](../../getting-started.md) guide. If so, you should have:

- [x] An existing Coinbase account
- [x] A configured API key
- [x] Python

- eth-brownie
- web3

### What is a Smart Contract?

To help us understand Smart Contracts, we can draw an analogy using a developer concept you are likely familiar with: APIs. 

APIs are contracts between a client and server, which yields for some nice parallels. Both APIs and Smart Contracts:

| **Aspect** | **APIs** | **Smart Contracts** |
|------------|----------|---------------------|
| Definition of rules/structure for how two parties interact | Valid requests and expected responses | Valid inputs and resulting actions |
| Deterministic | Server processes requests with predictable responses | Executes transactions according to logic with predictable result |
| Immutable and Versioned | Versioning for backward compatibility. Once an API is deployed, developers rely on its stability | Cannot be changed once deployed (similar to a fixed API version) |

### The value of Smart Contracts

While APIs rely on a centralized server, a Smart Contract differs in that its true value is in the nature of its decentralized environment. Because Smart Contracts run on the blockchain, this means:

- **[Trustless](https://academy.binance.com/en/glossary/trustless) Transactions:** Because Smart Contracts are immutable, promises are unbreakable. Invested parties only need to trust in the code instead of asking, "Can I trust this person?"

- **Transparency:** A deployed contract can be inspected by anyone on the blockchain. 

- **Automated:** Contract rules are enforced automatically without a middle man.

### Real-world use cases

Blah blah...

Continue reading to see this use case in action!

### Tools used

- Coinbase Developer Platform
    - Wallets
    - Transfers API
    - Coinbase Developer Platform Portal

While Smart Contracts come in multiple flavors, this guide will be using `ERC20` format.

??? question "What Smart Contract formats are available?" 

    - **ERC20:** A contract that keeps track of fungible tokens (any one token is exactly equal to any other token)
    - **ERC721:** A contract that keeps track of non-fungible tokens (where each token is unique, i.e., real estate or collectibles)
    - **ERC777:** ERC20, but with more sophisticated interactions via hooks and abstraction/simplification of token interactions.
    - **ERC1155:** Agnostic (fungible and non-fungible) contract with support for multiple types of tokens per contract.

    Read more in the [Open Zeppelin docs](https://docs.openzeppelin.com/contracts/3.x/tokens).

## Typical Smart Contract Workflow

Typically, to create and deploy an ERC20 Smart Contract involves many steps:

1. Creating the Solidity contract code
1. Implementing its required functions (`totalSupply`, `balanceof`, `transfer`, `approve`, `transferFrom`, etc. OpenZeppelin offers these implementations [out of the box](https://docs.openzeppelin.com/contracts/5.x/api/token/erc20)) and any custom features
1. Compiling the contract into bytecote for the [Ethereum Virtual Machine (EVM)](https://ethereum.org/en/developers/docs/evm/) to execute
1. Deploy the contract 
1. Finally, interact with the contract

As a recommendation, these steps should also include testing (using tools like `brownie` or `truffle`, creating unit tests, and running test deployments to a testnet).

??? question "What does an ERC20 contract look like?" 

    As an example, take a look at this (simplified) basic, bare bones example. Contracts are written using the [Solidity programming language](https://soliditylang.org/). We will continue going into the details throughout the rest of the tutorial, so don't focus on that too much. This is just to give you a general idea.

    ```sol title="SimpleToken.sol"
    // SPDX-License-Identifier: MIT
    pragma solidity ^0.8.0;

    contract SimpleToken {
        string public name = "SimpleToken";
        string public symbol = "STK";
        uint8 public decimals = 18;
        uint256 public totalSupply;
        mapping(address => uint256) public balanceOf;

        constructor(uint256 _initialSupply) {
            totalSupply = _initialSupply * 10 ** uint256(decimals);
            balanceOf[msg.sender] = totalSupply;
        }

        function transfer(address _to, uint256 _amount) public returns (bool) {
            require(balanceOf[msg.sender] >= _amount, "Insufficient balance");
            balanceOf[msg.sender] -= _amount;
            balanceOf[_to] += _amount;
            return true;
        }

        ...
    }
    ```

Keep reading and we will compare why the Coinbase Developer Platform SDK makes these process much easier.

## Coinbase Smart Contract Workflow

See how intensive a typical workflow is when creating even a basic Smart Contract? This is where the Coinbase Developer Platform SDK can really step in to alleviate you of your pain!

Coinbase provides SDKs and APIs to help simplify blockchain development which you can use to streamline the process and focus on other functionality.

Using Coinbase, you can create and deploy a Smart Contract with very minimal coding, leading to:

- **Easier use and faster development:** Skip time-consuming steps of writing contracts manually
- **Reduced risk:** Coinbase is a well-tested SDK which will help you avoid common errors or vulnerabilities
- **Focus on innovation:** Spend less time on low-level blockchain details since Coinbase abstracts much of this complexity away
- **Scalability:** Coinbase tools are designed to scale with your project, making it easier to grow with your user base

Let's get started.

## Step 1 -- Create and deploy a Smart Contract

That's right, it's just one step to create and deploy a Smart Contract using CDP's Wallet API!

Using a new or existing wallet, you can call Coinbase's `deploy_token` function which takes 3 parameters:

- A token name
- A token symbol
- Initial supply

And that's it!

??? question "Why do I need to create a token with the contract?"

    A Smart Contract needs tokens because the contract defines rules and behavior *for* transacting these tokens on the Ethereum blockchain. The ERC20 standard provides a set of functions that allow creation, transfer, or tracking of tokens within the Ethereum ecosystem. The Open Zeppelin implementation provides these out of the box and is inherited under-the-hood in the Coinbase API:

    - **`totalSupply`:** The total number of tokens that will ever exist
    - **`balanceOf`:** Returns the value of tokens owned by an account
    - **`transfer`:** Moves tokens from caller account to another account
    - **`allowance`**: Returns remaining number of tokens a spender is allowed to spend on behalf of the owner
    - **`approve`:** Sets an allowance of a spender
    - **`transferFrom`:** Moves a set amount of tokens from and to an address.

    See more information in the Open Zeppelin [API Reference](https://docs.openzeppelin.com/contracts/5.x/api/token/erc20#core).

    Creating tokens allows for a digital asset that can be used for in-game items, currency, and rewards. It also enables tokens to be integrated into decentralized exchanges, wallets, and other Ethereum applications across the ecosystem. 

As an example, let's assume you have already created (and funded) a wallet or imported an existing one. 

Once you define your token name, symbol, and initial supply, you can deploy the token as is:

```python
deployed_contract = wallet.deploy_token("GameCoin", "GAME". 100000)
deployed_contract.wait()
```

This will:

- Initialize your token named `Gamecoin` with a symbol of `GAME` and a cap of `100,000` tokens
- Deploy the ERC20 token contract 

All other required ECR20 functions are provided for you out of the box, as described in `"What Smart Contract formats are available?"` above.

## Step 2 -- Verify the contract was deployed in the CDP Portal

## Step 2 -- Interact with the contract in-game

## What to read next

...