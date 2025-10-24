#include "autocalibrate_button.h"

namespace esphome {
namespace ld2410 {

void AutocalibrateButton::press_action() { this->parent_->autocalibrate(); }

}  // namespace ld2410
}  // namespace esphome
