class Pyramid:
    def __init__(self, value):
        self.value = value

    def compress(self):
        while len(self.value) > 4:
            compressed_value = ""
            for i in range(0, len(self.value), 4):
                chunk = self.value[i:i+4]
                compressed_value += chunk[0]  # Take the first character from each 4-character chunk

            self.value = compressed_value

    def __str__(self):
        return self.value


class PyramidBuilder:
    @staticmethod
    def build_pyramid_from_file(input_filename):
        with open(input_filename, 'r') as file:
            input_string = file.read().strip()

        return Pyramid(input_string)

    @staticmethod
    def write_compressed_pyramid_to_file(output_filename, pyramid):
        with open(output_filename, 'w') as file:
            file.write(str(pyramid))


if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"

    pyramid_builder = PyramidBuilder()

    # Build Pyramid from file
    pyramid = pyramid_builder.build_pyramid_from_file(input_filename)

    # Compress Pyramid
    pyramid.compress()

    # Write compressed Pyramid to file
    pyramid_builder.write_compressed_pyramid_to_file(output_filename, pyramid)
