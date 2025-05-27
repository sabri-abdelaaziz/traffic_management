from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

env = StreamExecutionEnvironment.get_execution_environment()

# Simulate stream of agent types
data_stream = env.from_collection(
    collection=["bus", "tram", "taxi", "bus", "tram"],
    type_info=Types.STRING()
)

# Transform and log to stdout
data_stream.map(lambda agent: f"Simulated agent: {agent}").print()

env.execute("Simulate Agents Job")
