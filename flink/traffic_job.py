from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # Dummy test data
    data_stream = env.from_collection(
        collection=[
            ("vehicle_1", 34.056, -118.236),
            ("vehicle_2", 35.000, -119.000)
        ],
        type_info=Types.TUPLE([Types.STRING(), Types.DOUBLE(), Types.DOUBLE()])
    )

    data_stream \
        .map(lambda x: f"Vehicle {x[0]} at position ({x[1]:.5f}, {x[2]:.5f})") \
        .print()

    env.execute("Test Job")

if __name__ == "__main__":
    main()
