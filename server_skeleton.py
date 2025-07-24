#!/usr/bin/env python3
"""
Kafka MCP Server Skeleton - Workshop Template
A Model Context Protocol server for Kafka operations using FastMCP

This is a skeleton template for the Kafka MCP Server workshop.
Participants will implement the missing functionality step by step.
"""

import json
import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Any, Dict, Optional

from mcp.server.fastmcp import Context, FastMCP

# TODO: Import kafka utilities
# from kafka_utils import KafkaManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kafka-mcp-server")


@dataclass
class KafkaContext:
    """Application context holding Kafka manager"""
    kafka_manager: Optional['KafkaManager'] = None


# TODO: Create the FastMCP server with lifespan management
@asynccontextmanager
async def kafka_lifespan(server: FastMCP) -> AsyncIterator[KafkaContext]:
    """Manage Kafka connections lifecycle"""
    context = KafkaContext()
    try:
        logger.info("Starting Kafka MCP Server...")
        yield context
    finally:
        logger.info("Shutting down Kafka MCP Server...")
        # TODO: Add cleanup code here


# TODO: Initialize the MCP server


# TODO: Implement kafka_initialize_connection tool


# TODO: Implement kafka_list_topics tool


# TODO: Implement kafka_create_topic tool


# TODO: Implement kafka_delete_topic tool


# TODO: Implement kafka_get_topic_info tool


# TODO: Implement kafka_send_message tool


if __name__ == "__main__":
    # TODO: Run the server
    pass 