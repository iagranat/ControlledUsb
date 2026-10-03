import pcbnew
import sys

def check_layout():
    pcb_path = "d:/Projects/ControlledUsb/hardware/ControlledUsb.kicad_pcb"
    try:
        board = pcbnew.LoadBoard(pcb_path)
    except Exception as e:
        print(f"Failed to load board: {e}")
        return

    fps = list(board.GetFootprints())
    
    lset_f = pcbnew.LSET()
    lset_f.AddLayer(pcbnew.F_CrtYd)
    
    lset_b = pcbnew.LSET()
    lset_b.AddLayer(pcbnew.B_CrtYd)

    collisions = []
    
    # Check Courtyards
    for i in range(len(fps)):
        ref1 = fps[i].GetReference()
        
        # Check Front
        b1_f = fps[i].GetLayerBoundingBox(lset_f)
        if b1_f.GetWidth() > 0:
            for j in range(i + 1, len(fps)):
                b2_f = fps[j].GetLayerBoundingBox(lset_f)
                if b2_f.GetWidth() > 0 and b1_f.Intersects(b2_f):
                    ox = min(b1_f.GetX() + b1_f.GetWidth(), b2_f.GetX() + b2_f.GetWidth()) - max(b1_f.GetX(), b2_f.GetX())
                    oy = min(b1_f.GetY() + b1_f.GetHeight(), b2_f.GetY() + b2_f.GetHeight()) - max(b1_f.GetY(), b2_f.GetY())
                    if ox > 0.01e6 and oy > 0.01e6:
                        collisions.append(f"[F.CrtYd] {ref1} & {fps[j].GetReference()}: {ox/1e6:.2f}mm x {oy/1e6:.2f}mm")
        
        # Check Back
        b1_b = fps[i].GetLayerBoundingBox(lset_b)
        if b1_b.GetWidth() > 0:
            for j in range(i + 1, len(fps)):
                b2_b = fps[j].GetLayerBoundingBox(lset_b)
                if b2_b.GetWidth() > 0 and b1_b.Intersects(b2_b):
                    ox = min(b1_b.GetX() + b1_b.GetWidth(), b2_b.GetX() + b2_b.GetWidth()) - max(b1_b.GetX(), b2_b.GetX())
                    oy = min(b1_b.GetY() + b1_b.GetHeight(), b2_b.GetY() + b2_b.GetHeight()) - max(b1_b.GetY(), b2_b.GetY())
                    if ox > 0.01e6 and oy > 0.01e6:
                        collisions.append(f"[B.CrtYd] {ref1} & {fps[j].GetReference()}: {ox/1e6:.2f}mm x {oy/1e6:.2f}mm")

    if not collisions:
        print("ZERO Courtyard collisions detected. The layout looks perfect.")
    else:
        print(f"Found {len(collisions)} overlaps:")
        for c in collisions:
            print(c)

    # Let's also check if anything fell off the board visually (approximate bounding box: 100 to 165 X, 100 to 120 Y)
    out_of_bounds = []
    for fp in fps:
        pos = fp.GetPosition()
        x_mm = pos.x / 1e6
        y_mm = pos.y / 1e6
        ref = fp.GetReference()
        if x_mm < 95.0 or x_mm > 165.0 or y_mm < 95.0 or y_mm > 125.0:
            out_of_bounds.append(f"{ref} is at X:{x_mm:.1f} Y:{y_mm:.1f} (Seems out of bounds)")
            
    if out_of_bounds:
        print("\nWarnings:")
        for w in out_of_bounds:
            print(w)

if __name__ == '__main__':
    check_layout()
