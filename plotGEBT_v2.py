import matplotlib.pyplot as plt

def extract_points_data(file_path):
    points_data = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    point_started = False
    point_data = {}

    for line in lines:
        # print(line)
        if 'Point #:' in line:
            if point_data:
                points_data.append(point_data)
            point_data = {}
            point_started = True
            point_data['point'] = int(line.split()[-1])
        elif 'Member #:' in line:
            break
        elif point_started and '-----' not in line and line.strip():
            values = list(map(float, line.split()))
            # print(values)
            if 'coordinates' not in point_data:
                point_data['coordinates'] = values
            elif 'displacements' not in point_data:
                point_data['displacements'] = values[:3]
                point_data['rotations'] = values[3:6]
            else:
                # If additional data beyond required fields is needed, it can be added here
                pass

    if point_data:
        points_data.append(point_data)

    return points_data

def plot_graphs(points_data):
    points = [point['point'] for point in points_data]
    displacements = [point['displacements'] for point in points_data]
    rotations = [point['rotations'] for point in points_data]

    x_disp = [d[0] for d in displacements]
    y_disp = [d[1] for d in displacements]
    z_disp = [d[2] for d in displacements]

    x_rot = [r[0] for r in rotations]
    y_rot = [r[1] for r in rotations]
    z_rot = [r[2] for r in rotations]

    plt.figure(figsize=(12, 6))

    # Plot Displacements
    plt.subplot(1, 2, 1)
    plt.plot(points, x_disp, label='X1 Displacement')
    plt.plot(points, y_disp, label='X2 Displacement')
    plt.plot(points, z_disp, label='X3 Displacement')
    plt.xlabel('Point')
    plt.ylabel('Displacement')
    plt.title('Displacements along the Span')
    plt.legend()
    plt.grid(True)

    # Plot Rotations
    plt.subplot(1, 2, 2)
    plt.plot(points, x_rot, label='X1 Rotation')
    plt.plot(points, y_rot, label='X2 Rotation')
    plt.plot(points, z_rot, label='X3 Rotation')
    plt.xlabel('Point')
    plt.ylabel('Rotation')
    plt.title('Rotations along the Span')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# File path
file_path = 'C:/Users/bguth/Documents/DesEng4/01 Masters Project/01 Straight bar implementation/doink.dat.out'

# Extract data
points_data = extract_points_data(file_path)

# Plot graphs
plot_graphs(points_data)
