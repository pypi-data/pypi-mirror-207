# SPDX-FileCopyrightText: 2023-present dh031200 <imbird0312@gmail.com>
#
# SPDX-License-Identifier: AGPL-3.0-only
from .models import (
    init_model,
    pre_processing,
    device,
    post_processing,
    parse_args,
    get_name,
    save_dir,
    read,
    write,
)


def infer(src):
    net = init_model()
    image = pre_processing(src).to(device)
    result = net(image)
    output = post_processing(result, src)
    return output


def main():
    args = parse_args()
    src_name = get_name(args)
    output_prefix = save_dir(src_name)
    src = read(args)
    result = infer(src)
    write(f"{output_prefix / src_name}.png", result)


if __name__ == "__main__":
    main()
