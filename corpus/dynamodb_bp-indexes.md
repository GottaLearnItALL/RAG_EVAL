

# Best practices for using secondary indexes in DynamoDB
<a name="bp-indexes"></a>

Secondary indexes are often essential to support the query patterns that your application requires. At the same time, overusing secondary indexes or using them inefficiently can add cost and reduce performance unnecessarily.

**Contents**
+ [General guidelines for secondary indexes in DynamoDB](bp-indexes-general.md)
  + [Use indexes efficiently](bp-indexes-general.md#bp-indexes-general-efficiency)
  + [Choose projections carefully](bp-indexes-general.md#bp-indexes-general-projections)
  + [Optimize frequent queries to avoid fetches](bp-indexes-general.md#bp-indexes-general-fetches)
  + [Be aware of item-collection size limits when creating local secondary indexes](bp-indexes-general.md#bp-indexes-general-expanding-collections)
+ [Take advantage of sparse indexes](bp-indexes-general-sparse-indexes.md)
  + [Examples of sparse indexes in DynamoDB](bp-indexes-general-sparse-indexes.md#bp-indexes-sparse-examples)
+ [Using Global Secondary Indexes for materialized aggregation queries in DynamoDB](bp-gsi-aggregation.md)
  + [Example scenario and access patterns](bp-gsi-aggregation.md#bp-gsi-aggregation-scenario)
  + [Why pre-compute aggregations](bp-gsi-aggregation.md#bp-gsi-aggregation-why)
  + [Table design](bp-gsi-aggregation.md#bp-gsi-aggregation-table-design)
  + [Aggregation pipeline with Streams and AWS Lambda](bp-gsi-aggregation.md#bp-gsi-aggregation-pipeline)
  + [Sparse GSI design](bp-gsi-aggregation.md#bp-gsi-aggregation-sparse-gsi)
  + [Querying the GSI](bp-gsi-aggregation.md#bp-gsi-aggregation-querying)
  + [Considerations](bp-gsi-aggregation.md#bp-gsi-aggregation-considerations)
+ [Overloading Global Secondary Indexes in DynamoDB](bp-gsi-overloading.md)
+ [Using Global Secondary Index write sharding for selective table queries in DynamoDB](bp-indexes-gsi-sharding.md)
  + [Pattern design](bp-indexes-gsi-sharding.md#bp-indexes-gsi-sharding-pattern-design)
  + [Sharding strategy](bp-indexes-gsi-sharding.md#bp-indexes-gsi-sharding-strategy)
  + [Querying the sharded GSI](bp-indexes-gsi-sharding.md#bp-indexes-gsi-querying-the-sharded-GSI)
  + [Parallel query execution considerations](bp-indexes-gsi-sharding.md#bp-indexes-gsi-parallel-query-execution-considerations)
  + [Code example](bp-indexes-gsi-sharding.md#bp-indexes-gsi-code-example)
+ [Using Global Secondary Indexes to create an eventually consistent replica in DynamoDB](bp-indexes-gsi-replica.md)